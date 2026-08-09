# 🔬 AI Behavior & Evaluation Lab

Welcome to my independent research repository focusing on LLM cognitive tracing, behavioral biases, and reasoning scaffolding. This lab serves as a portfolio of structural diagnostics used to audit, map, and stress-test the alignment bounds of modern large language models.

## 📁 Active Research Papers & Evaluations

* [**Evaluation 01: The Illusion of Competence**](evals/false_encouragement_bias.md)
  * *Focus:* Mapping the systematic false-encouragement and "people-pleasing" bias in conversational models.
  * *Method:* Live multi-phase diagnostic traps.

* [**Evaluation 02: Diagnostic Reasoning in Claude Opus**](evals/opus_diagnostic_reasoning.md)
  * *Focus:* Analyzing self-referential reasoning, interpretive framing, and alignment deflection under conditions of high resistance.
  * *Method:* Iterative metacognitive auditing and line-by-line framework verification.

* [**Evaluation 03: Multi-Objective Tensions & Prompt-Induced Shifts**](evals/multi_objective_tensions.md)
  * *Focus:* Investigating how competing training objectives (truth vs. helpfulness) create friction inside the model's output distribution.
  * *Method:* Controlled prompt variants applied to a single base scenario using Grok 4.20.


## 🛠️ Automated Evaluation Tooling

* [**Multi-Prompt API Automation Script**](scripts/claude_basic_advice_test.py) CATEGORY: behavior, advice-giving
  * *Tooling:* Python script designed to execute parallel evaluation prompt arrays directly via the Anthropic API, bypassing standard user interface wrappers. 
 
* [**Multi-Prompt API Automation Script**](scripts/claude_boundry_test.py) CATEGORY: constraint handling, adversarial prompts, and relational behaviors.
  * *Tooling:* Python script designed to execute parallel evaluation prompt arrays directly via the Anthropic API, bypassing standard user interface wrappers. 
