Factory Audit
=============

Checking how various object factories perform in Django with respect to
creating valid instances out of the box.

.. image:: https://travis-ci.org/jamescooke/factory_audit.svg?branch=master
    :target: https://travis-ci.org/jamescooke/factory_audit

Definitions
-----------

* **Factory libraries**

  The following factory libraries have been explored:

  - `Factory Boy <https://github.com/FactoryBoy/factory_boy>`_

  - `Factory Djoy <https://github.com/jamescooke/factory_djoy>`_

  - `Hypothesis[django] <https://hypothesis.readthedocs.io/en/latest/django.html>`_

  - `Mixer <https://github.com/klen/mixer>`_

  - `Model Mommy <https://github.com/vandersonmota/model_mommy>`_


* **Models**

  Two factories have been created with each factory library:

  - ``ItemFactory``: to create and save instances of ``plant.models.Item``, a
    test model defined `in the 'plant' app
    </blob/master/factory_audit/plant/models.py>`_.

  - ``UserFactory``: to create and save instances of the default
    ``django.contrib.auth`` User Model.


* **Grading**

  Each factory is graded based on how its default configuration behaves.

  The gradings are based on the definition of "valid". Valid instances are ones
  which will pass Django's ``full_clean`` and not raise a ``ValidationError``.
  For example, using the ``ItemFactory`` a generated item passes validation
  with:

  .. code-block:: python

      item = ItemFactory()
      item.full_clean()

  The gradings are:

  - \:red_circle: RED - Factory creates **invalid** instances of the model and
    saves them to the database.

  - \:yellow_heart: YELLOW - Factory raises an exception and does not
    save any instances. Preferably this would be a ``ValidationError``, but
    I've also allowed ``IntegrityError`` here.

  - \:green_heart: GREEN - Factory creates multiple **valid** instances with no
    invalid instances created or skipped. Running factory ``n`` times generates
    ``n`` valid instances.


Results
-------

======================  ======================  ====================
Library                 ItemFactory             UserFactory
======================  ======================  ====================
**Factory Boy**         \:red_circle: RED       \:red_circle: RED
**Factory Djoy**        \:yellow_heart: YELLOW  \:green_heart: GREEN
**Hypothesis[django]**  \:red_circle: RED       \:red_circle: RED
**Mixer**               \:green_heart: GREEN    \:green_heart: GREEN
**Model Mommy**         \:yellow_heart: YELLOW  \:green_heart: GREEN
======================  ======================  ====================

For more detailed reasons for each grading see the individual test file for
each library.

* `Factory Boy </factory_audit/plant/tests/test_factory_boy_factories.py>`_

* `Factory Djoy </factory_audit/plant/tests/test_factory_djoy_factories.py>`_

* `Hypothesis[django] </factory_audit/plant/tests/test_hypothesis_factories.py>`_

* `Mixer </factory_audit/plant/mixer_tests.py>`_ (not in the test folder to
  hide them from Django's test runner's discovery).

* `Model Mommy </factory_audit/plant/tests/test_model_mommy_factories.py>`_


Contributions
-------------

Please add your own factory library and run it through the tests - pull
requests very welcome.

Please help me write a better wrapper for Hypothesis! I hypothesise that it
*is* possible!
