# coding=utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
from azure.core.exceptions import ResourceNotFoundError
from azure_devtools.scenario_tests import create_random_name
from azure.ai.metricsadvisor.models import (
    EmailHook,
    WebHook,
)
from base_testcase import TestMetricsAdvisorAdministrationClientBase


class TestMetricsAdvisorAdministrationClient(TestMetricsAdvisorAdministrationClientBase):

    def test_create_email_hook(self):
        email_hook_name = self.create_random_name(create_random_name("testemailhook"))
        try:
            email_hook = self.admin_client.create_hook(
                name=email_hook_name,
                hook=EmailHook(
                    emails_to_alert=["yournamehere@microsoft.com"],
                    description="my email hook",
                    external_link="external link"
                )
            )
            self.assertIsNotNone(email_hook.id)
            self.assertIsNotNone(email_hook.name)
            self.assertIsNotNone(email_hook.admins)
            self.assertEqual(email_hook.emails_to_alert, ["yournamehere@microsoft.com"])
            self.assertEqual(email_hook.description, "my email hook")
            self.assertEqual(email_hook.external_link, "external link")
            self.assertEqual(email_hook.hook_type, "Email")
        finally:
            self.admin_client.delete_hook(email_hook.id)

            with self.assertRaises(ResourceNotFoundError):
                self.admin_client.get_hook(email_hook.id)

    def test_create_web_hook(self):
        web_hook_name = self.create_random_name(create_random_name("testwebhook"))
        try:
            web_hook = self.admin_client.create_hook(
                name=web_hook_name,
                hook=WebHook(
                    endpoint="https://httpbin.org/post",
                    description="my web hook",
                    external_link="external link"
                )
            )
            self.assertIsNotNone(web_hook.id)
            self.assertIsNotNone(web_hook.name)
            self.assertIsNotNone(web_hook.admins)
            self.assertEqual(web_hook.endpoint, "https://httpbin.org/post")
            self.assertEqual(web_hook.description, "my web hook")
            self.assertEqual(web_hook.external_link, "external link")
            self.assertEqual(web_hook.hook_type, "Webhook")
        finally:
            self.admin_client.delete_hook(web_hook.id)

            with self.assertRaises(ResourceNotFoundError):
                self.admin_client.get_hook(web_hook.id)

    def test_list_hooks(self):
        hooks = self.admin_client.list_hooks()
        assert len(list(hooks)) > 0

    def test_update_email_hook_with_model(self):
        name = self.create_random_name(create_random_name("testwebhook"))
        try:
            hook = self._create_email_hook_for_update(name)
            name = self.get_replayable_random_resource_name("update")
            hook.name = name
            hook.description = "update"
            hook.external_link = "update"
            hook.emails_to_alert = ["myemail@m.com"]

            updated = self.admin_client.update_hook(hook)

            self.assertEqual(updated.name, name)
            self.assertEqual(updated.description, "update")
            self.assertEqual(updated.external_link, "update")
            self.assertEqual(updated.emails_to_alert, ["myemail@m.com"])

        finally:
            self.admin_client.delete_hook(hook.id)

    def test_update_email_hook_with_kwargs(self):
        name = self.create_random_name(create_random_name("testhook"))
        try:
            hook = self._create_email_hook_for_update(name)
            name = self.get_replayable_random_resource_name("update")
            updated = self.admin_client.update_hook(
                hook.id,
                hook_type="Email",
                name=name,
                description="update",
                external_link="update",
                emails_to_alert=["myemail@m.com"]
            )

            self.assertEqual(updated.name, name)
            self.assertEqual(updated.description, "update")
            self.assertEqual(updated.external_link, "update")
            self.assertEqual(updated.emails_to_alert, ["myemail@m.com"])

        finally:
            self.admin_client.delete_hook(hook.id)

    def test_update_email_hook_with_model_and_kwargs(self):
        name = self.create_random_name(create_random_name("testhook"))
        try:
            hook = self._create_email_hook_for_update(name)
            name = self.get_replayable_random_resource_name("updateme")
            hook.name = "don't update me"
            hook.description = "don't update me"
            hook.emails_to_alert = []
            updated = self.admin_client.update_hook(
                hook,
                hook_type="Email",
                name=name,
                description="update",
                external_link="update",
                emails_to_alert=["myemail@m.com"]
            )

            self.assertEqual(updated.name, name)
            self.assertEqual(updated.description, "update")
            self.assertEqual(updated.external_link, "update")
            self.assertEqual(updated.emails_to_alert, ["myemail@m.com"])

        finally:
            self.admin_client.delete_hook(hook.id)

    def test_update_email_hook_by_resetting_properties(self):
        name = self.create_random_name(create_random_name("testhook"))
        try:
            hook = self._create_email_hook_for_update(name)
            name = self.get_replayable_random_resource_name("reset")
            updated = self.admin_client.update_hook(
                hook.id,
                hook_type="Email",
                name=name,
                description=None,
                external_link=None,
            )

            self.assertEqual(updated.name, name)

            # sending null, but not clearing properties
            # self.assertEqual(updated.description, "")
            # self.assertEqual(updated.external_link, "")

        finally:
            self.admin_client.delete_hook(hook.id)

    def test_update_web_hook_with_model(self):
        name = self.create_random_name(create_random_name("testwebhook"))
        try:
            hook = self._create_web_hook_for_update(name)
            name = self.get_replayable_random_resource_name("hookupdate")
            hook.name = name
            hook.description = "update"
            hook.external_link = "update"
            hook.username = "myusername"
            hook.password = "password"

            updated = self.admin_client.update_hook(hook)

            self.assertEqual(updated.name, name)
            self.assertEqual(updated.description, "update")
            self.assertEqual(updated.external_link, "update")
            self.assertEqual(updated.username, "myusername")
            self.assertEqual(updated.password, "password")

        finally:
            self.admin_client.delete_hook(hook.id)

    def test_update_web_hook_with_kwargs(self):
        name = self.create_random_name(create_random_name("testwebhook"))
        try:
            hook = self._create_web_hook_for_update(name)
            name = self.get_replayable_random_resource_name("hookupdate")
            updated = self.admin_client.update_hook(
                hook.id,
                hook_type="Web",
                endpoint="https://httpbin.org/post",
                name=name,
                description="update",
                external_link="update",
                username="myusername",
                password="password"
            )

            self.assertEqual(updated.name, name)
            self.assertEqual(updated.description, "update")
            self.assertEqual(updated.external_link, "update")
            self.assertEqual(updated.username, "myusername")
            self.assertEqual(updated.password, "password")

        finally:
            self.admin_client.delete_hook(hook.id)

    def test_update_web_hook_with_model_and_kwargs(self):
        name = self.create_random_name(create_random_name("testwebhook"))
        try:
            hook = self._create_web_hook_for_update(name)
            name = self.get_replayable_random_resource_name("hookupdate")
            hook.name = "don't update me"
            hook.description = "updateMe"
            hook.username = "don't update me"
            hook.password = "don't update me"
            hook.endpoint = "don't update me"
            updated = self.admin_client.update_hook(
                hook,
                hook_type="Web",
                endpoint="https://httpbin.org/post",
                name=name,
                external_link="update",
                username="myusername",
                password="password"
            )

            self.assertEqual(updated.name, name)
            self.assertEqual(updated.description, "updateMe")
            self.assertEqual(updated.external_link, "update")
            self.assertEqual(updated.username, "myusername")
            self.assertEqual(updated.password, "password")

        finally:
            self.admin_client.delete_hook(hook.id)

    def test_update_web_hook_by_resetting_properties(self):
        name = self.create_random_name(create_random_name("testhook"))
        try:
            hook = self._create_web_hook_for_update(name)
            name = self.get_replayable_random_resource_name("reset")
            updated = self.admin_client.update_hook(
                hook.id,
                hook_type="Web",
                name=name,
                description=None,
                endpoint="https://httpbin.org/post",
                external_link=None,
                username="myusername",
                password=None
            )

            self.assertEqual(updated.name, name)
            self.assertEqual(updated.password, "")

            # sending null, but not clearing properties
            # self.assertEqual(updated.description, "")
            # self.assertEqual(updated.external_link, "")

        finally:
            self.admin_client.delete_hook(hook.id)
