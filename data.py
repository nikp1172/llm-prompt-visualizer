import os
import requests

TFY_API_KEY = os.environ.get('TFY_API_KEY')
TFY_HOST = os.environ.get('TFY_HOST', 'https://app.truefoundry.com')
ML_REPO_ID = os.environ.get('ML_REPO_ID', '688')
MODEL_NAME_VAR = os.environ.get('MODEL_NAME_VAR','model_name')
PROMPT_VAR = os.environ.get('PROMPT_VAR', 'prompt1')
RESPONSE_VAR = os.environ.get('RESPONSE_VAR', 'response1')
INFERENCE_TIME_VAR = os.environ.get('INFERENCE_TIME_VAR', 'inference_time')
USER_REACTION_VAR = os.environ.get('USER_REACTION_VAR', 'user_reaction')

def get_data():
    runs = requests.post(
        url=f'{TFY_HOST}/api/ml/api/2.0/mlflow/runs/search',
        json = {"experiment_ids": [ML_REPO_ID]},
        headers = {"Authorization": f"Bearer {TFY_API_KEY}"}
    ).json()
    data = []
    for run in runs['runs']:
        tags = run['data']['tags']
        tags = {tag1['key']: tag1['value'] for tag1 in tags}
        row = {}
        row['run_id'] = run['info']['run_id']
        row['model_name'] = tags.get(MODEL_NAME_VAR, "default")
        row['prompt'] = tags.get(PROMPT_VAR, 'empty')
        row['response'] = tags.get(RESPONSE_VAR, 'empty')
        row['inference_time'] = tags.get(INFERENCE_TIME_VAR, '')
        row['user_reaction'] = tags.get(USER_REACTION_VAR,'')
        data.append(row)
    return data

def update_changes_in_df(old_df, new_df):
    old_run_id_map = {old_df.iloc[i].run_id: old_df.iloc[i].user_reaction for i in range(len((old_df))) }
    new_run_id_map = {new_df.iloc[i].run_id: new_df.iloc[i].user_reaction for i in range(len((new_df))) }
    for key in old_run_id_map:
        if old_run_id_map[key] != new_run_id_map[key]:
            upd = requests.post(
                url=f'{TFY_HOST}/api/ml/api/2.0/mlflow/runs/set-tag',
                json = {"run_id": key, "key": USER_REACTION_VAR, "value": new_run_id_map[key]},
                headers = {"Authorization": f"Bearer {TFY_API_KEY}"}
            )
            if upd.status_code >= 300:
                print(f"Update Failed with error: {upd.text}")
