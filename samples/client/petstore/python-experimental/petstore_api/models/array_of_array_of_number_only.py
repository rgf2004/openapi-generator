# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint  # noqa: F401
import re  # noqa: F401

import six  # noqa: F401

from petstore_api.exceptions import ApiValueError  # noqa: F401
from petstore_api.model_utils import (  # noqa: F401
    ModelNormal,
    ModelSimple,
    check_allowed_values,
    check_validations
)


class ArrayOfArrayOfNumberOnly(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      openapi_types (dict): The key is attribute name
          and the value is attribute type.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
    """

    allowed_values = {
    }

    attribute_map = {
        'array_array_number': 'ArrayArrayNumber'  # noqa: E501
    }

    openapi_types = {
        'array_array_number': 'list[list[float]]'
    }

    validations = {
    }

    def __init__(self, array_array_number=None):  # noqa: E501
        """ArrayOfArrayOfNumberOnly - a model defined in OpenAPI"""  # noqa: E501

        self._array_array_number = None
        self.discriminator = None

        if array_array_number is not None:
            self.array_array_number = (
                array_array_number
            )

    @property
    def array_array_number(self):
        """Gets the array_array_number of this ArrayOfArrayOfNumberOnly.  # noqa: E501


        :return: The array_array_number of this ArrayOfArrayOfNumberOnly.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._array_array_number

    @array_array_number.setter
    def array_array_number(self, array_array_number):  # noqa: E501
        """Sets the array_array_number of this ArrayOfArrayOfNumberOnly.


        :param array_array_number: The array_array_number of this ArrayOfArrayOfNumberOnly.  # noqa: E501
        :type: list[list[float]]
        """

        self._array_array_number = (
            array_array_number
        )

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArrayOfArrayOfNumberOnly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other