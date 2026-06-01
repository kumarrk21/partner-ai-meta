# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from dotenv import load_dotenv

#---------------------------------------------------#
# Get Backend Config
#---------------------------------------------------#
def get_backend_config():
    load_dotenv()

    return {
        "PROJECT_ID": os.getenv("GOOGLE_CLOUD_PROJECT"),
        "BUCKET_NAME": os.getenv("BUCKET_NAME"),
        "IMAGE_FOLDER": os.getenv("IMAGE_FOLDER"),
        "DATA_FOLDER": os.getenv("DATA_FOLDER"),
        "PRODUCT_DATA_FILE": os.getenv("PRODUCT_DATA_FILE"),
        "CLOUD_RUN_SA": os.getenv("CLOUD_RUN_SA"),
        "IS_AGENT_LOCAL": os.getenv("LOCAL_AGENT", "False").lower() == "true",
        "APP_NAME": os.getenv("APP_NAME", "vogue_concierge_agent"),
        "LOCAL_PORT": int(os.getenv("LOCAL_PORT", 8000)),
        "AGENT_ENGINE_REGION": os.getenv("AGENT_ENGINE_REGION"),
        "AGENT_ENGINE_ID": os.getenv("AGENT_ENGINE_ID"),
    }
