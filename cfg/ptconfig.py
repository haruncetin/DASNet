import os
BASE_PATH='/content'
PTMODELS_ROOT= os.path.join(BASE_PATH, 'cd_res', 'pretrain')
if not os.path.exists(PTMODELS_ROOT):
    os.makedirs(PTMODELS_ROOT, exist_ok=True)

