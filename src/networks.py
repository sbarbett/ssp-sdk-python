# Copyright 2017 NeuStar, Inc.All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
from .network_id import NetworkId

class Networks:
	def __init__(self, connection, base_uri):
		self.connection = connection
		self.base_uri = base_uri+"/networks"

	def get(self):
		"""Get a list of Networks."""
		return self.connection.get(self.base_uri)

	def post(self, cidr1, cidr2, name):
		"""Create a new Network."""
		properties = {"cidr1": cidr1, "cidr2": cidr2, "name": name}
		return self.connection.post(self.base_uri, json.dumps(properties))

	def network_id(self, network_id):
		"""Create a Network Id object."""
		return NetworkId(self.connection, self.base_uri, network_id)

	def get_sponsor(self, sponsor_id):
		"""Get Network for a specific Sponsor."""
		return self.connection.get(self.base_uri+"/sponsor/"+sponsor_id)