# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class MediaGraphGrpcExtensionDataTransferMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """How frame data should be transmitted to the inference engine.
    """

    EMBEDDED = "Embedded"  #: Frames are transferred embedded into the gRPC messages.
    SHARED_MEMORY = "SharedMemory"  #: Frames are transferred through shared memory.

class MediaGraphImageFormatRawPixelFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The pixel format that will be used to encode images.
    """

    YUV420_P = "Yuv420p"  #: Planar YUV 4:2:0, 12bpp, (1 Cr and Cb sample per 2x2 Y samples).
    RGB565_BE = "Rgb565be"  #: Packed RGB 5:6:5, 16bpp, (msb)   5R 6G 5B(lsb), big-endian.
    RGB565_LE = "Rgb565le"  #: Packed RGB 5:6:5, 16bpp, (msb)   5R 6G 5B(lsb), little-endian.
    RGB555_BE = "Rgb555be"  #: Packed RGB 5:5:5, 16bpp, (msb)1X 5R 5G 5B(lsb), big-endian , X=unused/undefined.
    RGB555_LE = "Rgb555le"  #: Packed RGB 5:5:5, 16bpp, (msb)1X 5R 5G 5B(lsb), little-endian, X=unused/undefined.
    RGB24 = "Rgb24"  #: Packed RGB 8:8:8, 24bpp, RGBRGB.
    BGR24 = "Bgr24"  #: Packed RGB 8:8:8, 24bpp, BGRBGR.
    ARGB = "Argb"  #: Packed ARGB 8:8:8:8, 32bpp, ARGBARGB.
    RGBA = "Rgba"  #: Packed RGBA 8:8:8:8, 32bpp, RGBARGBA.
    ABGR = "Abgr"  #: Packed ABGR 8:8:8:8, 32bpp, ABGRABGR.
    BGRA = "Bgra"  #: Packed BGRA 8:8:8:8, 32bpp, BGRABGRA.

class MediaGraphImageScaleMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the modes for scaling an input video frame into an image, before it is sent to an
    inference engine.
    """

    PRESERVE_ASPECT_RATIO = "PreserveAspectRatio"  #: Use the same aspect ratio as the input frame.
    PAD = "Pad"  #: Center pad the input frame to match the given dimensions.
    STRETCH = "Stretch"  #: Stretch input frame to match given dimensions.

class MediaGraphInstanceState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Allowed states for a graph instance.
    """

    INACTIVE = "Inactive"  #: The media graph instance is idle and not processing media.
    ACTIVATING = "Activating"  #: The media graph instance is transitioning into the active state.
    ACTIVE = "Active"  #: The media graph instance is active and processing media.
    DEACTIVATING = "Deactivating"  #: The media graph instance is transitioning into the inactive state.

class MediaGraphMotionDetectionSensitivity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enumeration that specifies the sensitivity of the motion detection processor.
    """

    LOW = "Low"  #: Low Sensitivity.
    MEDIUM = "Medium"  #: Medium Sensitivity.
    HIGH = "High"  #: High Sensitivity.

class MediaGraphOutputSelectorOperator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The operator to compare streams by.
    """

    IS_ENUM = "is"  #: A media type is the same type or a subtype.
    IS_NOT = "isNot"  #: A media type is not the same type or a subtype.

class MediaGraphParameterType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the parameter.
    """

    STRING = "String"  #: A string parameter value.
    SECRET_STRING = "SecretString"  #: A string to hold sensitive information as parameter value.
    INT = "Int"  #: A 32-bit signed integer as parameter value.
    DOUBLE = "Double"  #: A 64-bit double-precision floating point type as parameter value.
    BOOL = "Bool"  #: A boolean value that is either true or false.

class MediaGraphRtspTransport(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Underlying RTSP transport. This is used to enable or disable HTTP tunneling.
    """

    HTTP = "Http"  #: HTTP/HTTPS transport. This should be used when HTTP tunneling is desired.
    TCP = "Tcp"  #: TCP transport. This should be used when HTTP tunneling is NOT desired.
