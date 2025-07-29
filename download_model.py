#使用python的huggingface_hub函数下载
from huggingface_hub import snapshot_download
#repo_id填写LanguageBind/Open-Sora-Plan-v1.3.0和mt5-xxl
download_path1 = snapshot_download(repo_id="LanguageBind/Open-Sora-Plan-v1.3.0", local_dir="./Open-Sora-Plan-v1.3.0")
download_path2 = snapshot_download(repo_id="google/mt5-xxl", local_dir="./mt5-xxl")
