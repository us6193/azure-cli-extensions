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
    "billing department",
)
class __CMDGroup(AAZCommandGroup):
    """Get and List operations at billing account scope to identify Departments and is only for EA customers
    """
    pass


__all__ = ["__CMDGroup"]
