# Hi, I'm Srivatsa 👋

I build the unglamorous half of software: the pipelines, the infrastructure, and the AI systems that have to keep working after the demo crowd goes home. Most of what I do lives in the gap between "it runs on my machine" and "it survives production at 3am."

Right now I'm wrapping up my MS in Computer Science at the University of Illinois Chicago (GPA 3.88), where I've spent two years split between research infrastructure and AI platform engineering. Before that I was an engineer at Mu Sigma, mostly resurrecting data pipelines people had quietly given up on.

I hold a granted patent, a handful of merged fixes in OSS frameworks you've probably imported, and a fairly strong opinion that observability is not optional.

## What I'm actually good at

- **Cloud & DevOps:** Kubernetes, Terraform, and CI/CD that doesn't flake. I once took per-node setup from 4 hours down to 45 minutes and called it a Tuesday.
- **AI platforms:** RAG and Graph-RAG systems, LLM agents, and retrieval that actually cites its sources instead of making things up.
- **Backend & data:** Python/FastAPI services, polling-to-event-driven rewrites, and Postgres queries dragged from ~800ms down to under 150ms.
- **Research infra:** reproducible fuzzing pipelines and Bayesian residual-risk estimators (yes, the real statistics kind).

## Things I've built (and will happily defend in an interview)

**[ECI Pipeline](https://github.com/Srivatsa03/ECI-Pipeline)**: DeltaRAG + Graph-RAG that watches 10 live Android security and CVE feeds and writes evidence-backed risk tickets for fraud teams. 93% retrieval precision, sub-second monitoring dashboard. *(TransUnion industry capstone)*

**MetARAG**: Document-intelligence platform: ask plain-English questions across 100+ GB of PDFs and get answers with their sources attached. 93% retrieval precision, 40% faster responses, built leading a team of 5. *(CCC Intelligent Solutions capstone, code under NDA)*

**[End-to-End DevSecOps on EKS](https://github.com/Srivatsa03/End-to-End-Kubernetes-Three-Tier-DevSecOps-Project)**: An 8-microservice platform on AWS EKS with Jenkins + ArgoCD and Trivy/SonarQube security gates. Handles 500+ req/sec with zero-downtime deploys.

**[Movie Recommendation MLOps](https://github.com/Srivatsa03/Movie-Recommendation)**: The full lifecycle, not just a notebook: training, serving, A/B tests, drift detection, and Prometheus/Grafana dashboards. RMSE 0.58.

**[CoT vs Answer-Only on CLEVR](https://github.com/Srivatsa03/Chain-of-Thought-on-CLEVR)**: Fine-tuned BLIP-2 with LoRA on an NVIDIA L40S, pushing accuracy from 8.75% zero-shot to 45.95%, then mapped exactly where chain-of-thought helps reasoning and where it quietly hurts.

**[Counterfactual Fact Verification](https://github.com/Srivatsa03/Counterfactual_Fact_Checking)**: Zero-shot fact-checking on FEVER with local quantized LLMs (Phi-3 Mini, Llama 3.1 8B, Mistral 7B). I generate counterfactual claim variants across complexity tiers to test where small models stay honest and where they break. *(ongoing research)*

## Open source

Those repos that look like forks of LiteLLM, LlamaIndex, and Haystack? That's where I actually fixed things. I like finding the bug everyone else scrolled past.

- **[Haystack](https://github.com/deepset-ai/haystack/pull/11670)** (20k★): silenced noisy ERROR logs that fired on empty inputs. *PR #11670, merged.*
- **[LiteLLM](https://github.com/BerriAI/litellm/pull/30764)** (48k★): fixed a masker that leaked short secrets (8 chars or fewer) straight into logs and the admin UI. *PR #30764, merged.*
- **[LiteLLM](https://github.com/BerriAI/litellm/pull/29693)** (48k★): corrected a 10x embedding-pricing error that was inflating everyone's cost reports. *PR #29693, merged.*
- **[LlamaIndex](https://github.com/run-llama/llama_index/pull/22046)**: fixed silent data loss where all but the last chunk of a document was dropped on upsert. *PR #22046, open / under review.*

## What I'm building right now

- Pushing telemetry collection from minute-scale polling to event-driven, sub-second delivery.
- Making Graph-RAG earn its name instead of being "vector search with extra steps."
- Reading far too much about how to make LLM agents fail loudly instead of silently.

## Tech I reach for

```
Languages     Python · JavaScript/TypeScript · Java · C++ · SQL · Scala
Cloud & infra AWS · Azure · GCP · Kubernetes · Docker · Terraform · Ansible
CI/CD         Jenkins · GitHub Actions · ArgoCD
AI / ML       LangChain · OpenAI APIs · PyTorch · pgvector · RAG / Graph-RAG
Backend       FastAPI · Node.js · React / Next.js · PostgreSQL · Redis
Observability Prometheus · Grafana · Loki
```

## One patent, for the curious

**Book Issue Management System for Libraries** (IP India, granted Nov 2023, co-invented): AI cameras, RFID, and automated access control for hands-off library check-in and return.

## Reach me

I'm open to full-time **Software Engineering**, **Platform / Infrastructure**, and **AI Engineering** roles across the US.

- 📧 **Email:** srivatsakamballa02@gmail.com
- 💼 **LinkedIn:** [linkedin.com/in/srivatsa-kamballa](https://linkedin.com/in/srivatsa-kamballa)
- 🌐 **Portfolio:** [srivatsa03.github.io/My-Portfolio](https://srivatsa03.github.io/My-Portfolio)

Email or a LinkedIn DM both work. I read both, and I actually reply.

<!--
  OPTIONAL: a stats card showcases your real commits, stars, and PRs.
  It quietly counters the "1 follower, looks inactive" first impression.
  Uncomment to use:

  ![Srivatsa's GitHub stats](https://github-readme-stats.vercel.app/api?username=Srivatsa03&show_icons=true&hide_rank=true&include_all_commits=true)
-->
