#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Ryan Shim, Gilbert

import rclpy

from ubot_example.ubot_example.ubot_patrol_server.ubot_patrol_server \
    import UbotPatrolServer


def main(args=None):
    rclpy.init(args=args)
    ubot_patrol_server = UbotPatrolServer()
    rclpy.spin(ubot_patrol_server)

    ubot_patrol_server.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()