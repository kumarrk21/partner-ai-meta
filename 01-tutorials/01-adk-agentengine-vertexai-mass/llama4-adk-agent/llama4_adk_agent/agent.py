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

from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from .tools import (
    get_exchange_rate
)

root_agent = Agent(
    model = LiteLlm(model="vertex_ai/meta/llama-3.3-70b-instruct-maas"), # 3.3 Model
    # model=LiteLlm(model="vertex_ai/meta/llama-4-scout-17b-16e-instruct-maas"),  # Scout model
    # model=LiteLlm(model="vertex_ai/meta/llama-4-maverick-17b-128e-instruct-maas"), # Maverick model
    name='llama4_adk_agent',
    description='A helpful assistant for user questions including currency exchange rates',
    instruction='Answer user questions to the best of your knowledge. Use tools available to you if needed.',
    tools=[get_exchange_rate],
)