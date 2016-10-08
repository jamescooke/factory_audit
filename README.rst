Factory Audit
=============

Checking how various object factories perform in Django with respect to
creating valid instances.

Definitions
-----------

* **Factory libraries**

  The following factory libraries have been explored:

  - `Factory Boy <https://github.com/FactoryBoy/factory_boy>`_

  - `Factory Djoy <https://github.com/jamescooke/factory_djoy>`_


* **Models**

  Two factories have been created with each factory library:

  - ``ItemFactory``: to create and save instances of ``plant.models.Item``, a
    test model defined `in the 'plant' app
    </blob/master/factory_audit/plant/models.py>`_.

  - ``UserFactory``: to create and save instances of the default
    ``django.contrib.auth`` User Model.


* **Grading**

  Each factory is graded based on how its default configuration behaves. The
  gradings are:

  - RED :red_circle: - Factory creates invalid instances of the model and saves
    them to the database.

  - YELLOW :yellow_heart: - Factory raises a ``ValidationError`` and does not
    save any instances.

  - GREEN :green_heart: - Factory creates multiple valid instances for the user
    with its own strategy.


Results
-------

============  ======================  ====================
Factory       ItemFactory             UserFactory
============  ======================  ====================
Factory Boy   RED :red_circle:        RED :red_circle:
Factory Djoy  YELLOW :yellow_heart:   GREEN :green_heart:
============  ======================  ====================


Contributions
-------------

Please add your own factory library and run it through the tests - pull
requests very welcome.
