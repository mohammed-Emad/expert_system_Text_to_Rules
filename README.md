# expert_system_Text_to_Rules
Preparation of data for expert system Text conversion to facts and Rules and to use

What about the project

The project talks about temperature control based on human experience. The data are random data and the method is incorrect. But I  wrote it may be inspiring for another job
You should benefit here from the general concept

The idea is to convert a text file into a set of facts
__It means converting the file written by the expert here /data/data_expert.txt__

```
%% The rule :: Decision taken

temperature 50 :: heater 300
temperature 156 :: heater 1221
temperature 36 :: heater 820
temperature 129 :: heater 115
temperature 166 :: heater 1124
temperature 136 :: heater 776
temperature 88 :: heater 409
```

,convert it to a Python code that contains the facts.
As the file :compiled_knowledge.py

```
from pyknow import *

class engine(KnowledgeEngine):

	@Rule(Fact(temperature = 50))
	def fact_P0(self):
		heater = 300
		print('heater :=', heater)
		''' Here write the rest of your operations and orders '''


	@Rule(Fact(temperature = 156))
	def fact_P1(self):
		heater = 1221
		print('heater :=', heater)
		''' Here write the rest of your operations and orders '''


	@Rule(Fact(temperature = 36))
	def fact_P2(self):
		heater = 820
		print('heater :=', heater)
		''' Here write the rest of your operations and orders '''

```
This conversion is done using the file compile.py

It is the task of translating the expert file into facts. Note that comments can be written to the expert file via %% tags
You must type two tags.

You can change your writing style any way you like



The use of text string tools in general to search for spaces and words and then rewriting the rules and facts in the file as a code with the taking into account the distances of Python

After reading these lines, you can reuse them better
Library pyknow



*Use*
get the expert file ؟data_expert.txt

and run 
```
python3 compile.py
```
The file will produce us with its rules
compiled_knowledge.py

Then we can test

``` python
from pyknow import *
import compiled_knowledge



engine = compiled_knowledge.engine()
engine.reset() # Prepare the engine for the execution.
engine.declare(Fact(temperature = 105))
engine.declare(Fact(temperature = 36))
engine.run()

```


You can browse the code and read it and I am sure you will begin to modify it to comply with you


[pyknow](https://github.com/buguroo/pyknow)

You have written the full details of this but in Arabic you can see it  [here](https://github.com/mohammed-Emad/expert_system_Text_to_Rules/blob/master/Arabic_details.md)
