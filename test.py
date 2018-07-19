from pyknow import *
import compiled_knowledge



engine = compiled_knowledge.engine()
engine.reset() # Prepare the engine for the execution.
engine.declare(Fact(temperature = 105))
engine.declare(Fact(temperature = 36))
engine.run()

print(engine.facts)

