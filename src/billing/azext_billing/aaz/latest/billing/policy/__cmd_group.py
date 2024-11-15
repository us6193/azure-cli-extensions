# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "billing policy",
)
class __CMDGroup(AAZCommandGroup):
    """Multiple operations ( Get, List, Create) at different scopes around policies and is only for customers on MCA and MPA
    """
    pass


__all__ = ["__CMDGroup"]
