Welcome to immutabledict’s documentation!
=========================================

This site covers immutabledict’s API documentation for version |release|. For more information about immutabledict, see `the Github repository <https://github.com/corenting/immutabledict>`_.

Usage
-----

The :class:`.immutabledict`  class can be used as a drop-in replacement for :class:`dict`.

For replacing an :class:`collections.OrderedDict`, you can use an :class:`.ImmutableOrderedDict`. The API is the same as :class:`.immutabledict`, but it will use an :class:`collections.OrderedDict` under the hood.

.. code-block:: python

   from immutabledict import immutabledict

   my_item = immutabledict({"a": "value", "b": "other_value"})
   print(my_item["a"]) # Print "value"

Some additional methods are provided, see the API reference.


API reference
-------------

.. toctree::
   :maxdepth: 1

   /api/immutabledict
   /api/immutable_ordered_dict
   changelog

