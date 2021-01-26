# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest
from azure.ai.formrecognizer._helpers import get_content_type
from testcase import FormRecognizerTest

@pytest.mark.skip
class TestContentType(FormRecognizerTest):

    def test_pdf(self):
        with open(self.invoice_pdf, "rb") as fd:
            content_type = get_content_type(fd)
        self.assertEqual(content_type, "application/pdf")

    def test_pdf_bytes(self):
        with open(self.invoice_pdf, "rb") as fd:
            myfile = fd.read()
        content_type = get_content_type(myfile)
        self.assertEqual(content_type, "application/pdf")

    def test_jpg(self):
        with open(self.form_jpg, "rb") as fd:
            content_type = get_content_type(fd)
        self.assertEqual(content_type, "image/jpeg")

    def test_jpg_bytes(self):
        with open(self.form_jpg, "rb") as fd:
            myfile = fd.read()
        content_type = get_content_type(myfile)
        self.assertEqual(content_type, "image/jpeg")

    def test_png(self):
        with open(self.receipt_png, "rb") as fd:
            content_type = get_content_type(fd)
        self.assertEqual(content_type, "image/png")

    def test_png_bytes(self):
        with open(self.receipt_png, "rb") as fd:
            myfile = fd.read()
        content_type = get_content_type(myfile)
        self.assertEqual(content_type, "image/png")

    def test_tiff_little_endian(self):
        with open(self.invoice_tiff, "rb") as fd:
            content_type = get_content_type(fd)
        self.assertEqual(content_type, "image/tiff")

    def test_tiff_little_endian_bytes(self):
        with open(self.invoice_tiff, "rb") as fd:
            myfile = fd.read()
        content_type = get_content_type(myfile)
        self.assertEqual(content_type, "image/tiff")

    def test_tiff_big_endian(self):
        content_type = get_content_type(b"\x4D\x4D\x00\x2A")
        self.assertEqual(content_type, "image/tiff")

    def test_bmp(self):
        content_type = get_content_type(b"\x42\x4D\x00\x00")
        self.assertEqual(content_type, "image/bmp")
