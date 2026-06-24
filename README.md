<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=3000&pause=800&color=26D0CE&center=true&vCenter=true&width=640&lines=Platform+%2B+AI+Engineer;I+make+infrastructure+boring+on+purpose;RAG+systems+that+cite+their+sources;Open-source+bug-fixer+in+48k%E2%98%85+repos" alt="Typing SVG" />
  </a>
</p>

# Hi, I'm Srivatsa 👋

I build the unglamorous half of software: the pipelines, the infrastructure, and the AI systems that have to keep working after the demo crowd goes home. Most of what I do lives in the gap between "it runs on my machine" and "it survives production at 3am."

Right now I'm wrapping up my MS in Computer Science at the University of Illinois Chicago (GPA 3.88), where I've spent two years split between research infrastructure and AI platform engineering. Before that I was an engineer at Mu Sigma, mostly resurrecting data pipelines people had quietly given up on.

I hold a granted patent, a handful of merged fixes in OSS frameworks you've probably imported, and a fairly strong opinion that observability is not optional.

<p align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=Srivatsa03&show_icons=true&include_all_commits=true&hide_rank=true&theme=tokyonight&hide_border=true&bg_color=00000000" alt="GitHub stats" />
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Srivatsa03&layout=compact&langs_count=8&theme=tokyonight&hide_border=true&bg_color=00000000&hide=jupyter%20notebook,html,tex" alt="Top languages" />
</p>

## What I'm actually good at

- **Cloud & DevOps:** Kubernetes, Terraform, and CI/CD that doesn't flake. I once took per-node setup from 4 hours down to 45 minutes and called it a Tuesday.
- **AI platforms:** RAG and Graph-RAG systems, LLM agents, and retrieval that actually cites its sources instead of making things up.
- **Backend & data:** Python/FastAPI services, polling-to-event-driven rewrites, and Postgres queries dragged from ~800ms down to under 150ms.
- **Research infra:** reproducible fuzzing pipelines and Bayesian residual-risk estimators (yes, the real statistics kind).

## Things I've built (and will happily defend in an interview)

<p align="center">
  <a href="https://github.com/Srivatsa03/ECI-Pipeline">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Srivatsa03&repo=ECI-Pipeline&theme=tokyonight&hide_border=true&bg_color=00000000" alt="ECI Pipeline" />
  </a>
  <a href="https://github.com/Srivatsa03/End-to-End-Kubernetes-Three-Tier-DevSecOps-Project">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Srivatsa03&repo=End-to-End-Kubernetes-Three-Tier-DevSecOps-Project&theme=tokyonight&hide_border=true&bg_color=00000000" alt="DevSecOps on EKS" />
  </a>
</p>

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

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![Scala](https://img.shields.io/badge/Scala-DC322F?style=for-the-badge&logo=scala&logoColor=white)

**Cloud & DevOps**

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)

**AI / ML**

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![pgvector](https://img.shields.io/badge/pgvector-336791?style=for-the-badge&logo=postgresql&logoColor=white)

**Backend & Data**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=for-the-badge&logo=redis&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

## My GitHub, visualized

[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=Srivatsa03&theme=tokyo-night&hide_border=true&bg_color=00000000&custom_title=Contribution%20Activity)](https://github.com/Srivatsa03)

![snake animation](https://raw.githubusercontent.com/Srivatsa03/Srivatsa03/output/github-snake-dark.svg)

<!--
  OPTIONAL streak card. Add back once you confirm your daily streak looks good:
  <p align="center">
    <img src="https://streak-stats.demolab.com?user=Srivatsa03&theme=tokyonight&hide_border=true&background=00000000" height="170" />
  </p>
-->

## One patent, for the curious

**Book Issue Management System for Libraries** (IP India, granted Nov 2023, co-invented): AI cameras, RFID, and automated access control for hands-off library check-in and return.

## Reach me

I'm open to full-time **Software Engineering**, **Platform / Infrastructure**, and **AI Engineering** roles across the US.

[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:srivatsakamballa02@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/srivatsa-kamballa)
[![Portfolio](https://img.shields.io/badge/Portfolio-26D0CE?style=for-the-badge&logo=googlechrome&logoColor=white)](https://srivatsa03.github.io/My-Portfolio)

Email or a LinkedIn DM both work. I read both, and I actually reply.
