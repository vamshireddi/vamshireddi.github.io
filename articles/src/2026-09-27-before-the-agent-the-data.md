---
title: Before the Agent, the Data
subtitle: Why I sat the Salesforce Data 360 Consultant exam two weeks after B2C, and why Dreamforce 2026 put the data layer underneath everything from Agentforce to AIforce and Claudeforce
date: 2026-09-27 09:00
toc: true
summary: I earned the Salesforce Certified Data 360 Consultant credential this week, two weeks after B2C Solution Architect and days after a Dreamforce that took the whole platform headless. AIforce, Claudeforce, Agentforce and the Headless Toolkit make Salesforce reachable from anywhere an agent works, and every one of them reads from the same place, Data 360. Here is how I think about building that foundation so the agents on top of it can be trusted.
tags: [Salesforce, Data 360, Agentforce, AIforce, Architecture, AI, Manufacturing]
cover: /articles/images/data-360-consultant-certificate.jpg
cover_alt: Salesforce Certified Data 360 Consultant certificate presented to Vamshi Krishna Reddy Bandaru, issued September 26, 2026, credential ID 8164566
---

Two weeks ago I wrote that [the customer is the architecture](/articles/b2c-solution-architect/), and that in any multi-cloud Salesforce program Data 360 is the spine everything else hangs from. This week I sat the exam that tests whether you can actually build that spine. I passed, and I'm now a Salesforce Certified Data 360 Consultant.

The timing matters. The exam came days after a Dreamforce where Salesforce stopped treating its own screens as the center of the platform. AIforce brings Salesforce into Claude, Slack and Lightning. The Headless Toolkit turns every capability into an API, an MCP tool or a command. Agentforce agents can now reason on Claude or on Salesforce's own new model, Koa. Look underneath any of those announcements and you find the same thing: Data 360, supplying the context. The more places an agent can act, the more it matters that what it knows is right.

A fair question is why someone who already holds the Systems Architect, Application Architect and B2C Solution Architect credentials would sit a consultant exam. The architect exams test whether you know where Data 360 belongs in a design. This one tests whether you know how it behaves once real data arrives. In 2026 that second skill is where AI programs are being won and lost.

The exam's weighting makes the point. Data Activations and Utilization is 20%. Data Source Connection and Ingestion is 18%. Data Enhancements, Sharing, and Analysis is 18%. Harmonization and Unification is 17%. Solution Positioning is 14%, and Data 360 Setup and Administration is 13%. More than half of it is about getting data in, making it agree with itself, and putting it to work.

A note on names, because they keep moving. Salesforce renamed Data Cloud to Data 360 at Dreamforce in October 2025, as the data layer of Agentforce 360, and the certification took the new name in March 2026 with the same exam code. [Verify the credential](https://sforce.co/verifycerts): credential ID 8164566, issued September 26, 2026. Terms are spelled out in the [glossary at the end](#appendix-glossary).

## The stack after Dreamforce 2026

![The Salesforce agentic stack after Dreamforce 2026: AIforce surfaces, the Headless Toolkit, agents and reasoning, Data 360 context, and systems of record, wrapped by the Trusted Enterprise AI Harness](/articles/images/agentic-stack-2026.svg)

Dreamforce 2026 produced a lot of new names. Set side by side, they form a stack, and it reads best from the top down.

**Surfaces.** AIforce, announced on September 15, is Salesforce's layer for bringing its data, workflows and logic to wherever people and agents already work. It launched with three surfaces. Claudeforce, the Salesforce and Anthropic partnership, puts Salesforce inside Claude, and has been open to all customers in beta since Dreamforce. Slackforce brings it into Slack. Agentforce Coworker brings it into Lightning and is available now.

**Headless.** Underneath AIforce is what Salesforce now calls the Headless Toolkit, introduced as Headless 360 at TDX in April. The idea is simple: every capability on the platform is exposed as an API, an MCP tool or a command-line action, so an agent doesn't need a screen to use it. Headless Data 360, announced in August, does the same for data, exposing more than 200 Data 360 APIs to agents over MCP. In the B2C article I argued that headless had stopped being a preference and become a requirement. Dreamforce made that true for the whole platform.

**Agents and reasoning.** Agentforce is still where agents are built and run, with subagents (called topics until April), multi-agent orchestration and a growing set of job-ready agents. The model underneath is becoming a choice. Claude serves as a reasoning model for Agentforce's Atlas Reasoning Engine and is the default in Agentforce Coworker. Koa, Salesforce's CRM reasoning model built on NVIDIA Nemotron, is in pilot, with general availability expected this winter. MuleSoft Agent Fabric governs and orchestrates agents across systems, including agents Salesforce didn't build.

**Context.** This is Data 360: harmonized, unified and federated data, plus the new Agent Context Engine, which assembles governed, authorized context for an agent across relational, profile, search, graph and federated sources. It was announced at Dreamforce, with general availability expected later this year.

**Systems of record.** The ERP, dealer and distributor systems, service and warranty, connected products and the data lake. Dreamforce doesn't change them, and it shouldn't have to.

Salesforce wraps all of this in what it calls the Trusted Enterprise AI Harness, covering context, agency, action, governance, security and models, with a new AI Control Plane for seeing and managing agents across the enterprise. The foundations exist today, and the unified experience rolls out from early in Salesforce's fiscal 2028.

Here is what I take from the stack. The top layers are multiplying. A year ago an agent lived inside one Salesforce interface. Now the same customer record might be read by an agent in Claude, a bot in Slack, a coworker in Lightning and a partner's agent over MCP, all in the same afternoon. Every one of them grounds on layer four. Headless doesn't make the data layer less important. It removes the last screen that used to hide its mistakes.

## Inside the data layer: five stages from source to agent

![Data 360 reference flow: enterprise sources, ingestion, harmonization, unification, and activation for people and agents, with governance across every stage](/articles/images/data-360-reference-flow.svg)

Inside Data 360, I draw the work as a flow from left to right, because that's the order the problems show up in.

**Sources** are everything the enterprise already runs: the Salesforce clouds, an ERP, dealer or distributor systems, service and warranty, connected-product telemetry, and very often a data lake that another team owns. None of them agree on who the customer is.

**Ingestion** brings that data in through data streams, whether from native connectors, the Ingestion API, MuleSoft or cloud storage. It lands first in data lake objects, in essentially the shape the source sent it. Some of it never needs to land at all, which is what zero copy is for.

**Harmonization** maps those raw objects onto data model objects in a common model. This is where "account," "customer," "dealer" and "sold-to party" either get reconciled into shared definitions or quietly don't.

**Unification** runs identity resolution. Match rules decide which records are the same person or company, and reconciliation rules decide which value wins when they disagree. The output is a unified profile.

**Activation** is where the value finally shows up: calculated and streaming insights, segments sent to marketing and advertising targets, data actions that trigger flows, and grounding for Agentforce and for every other agent that now reads through AIforce or MCP.

Every stage runs under the same governance: data spaces that separate brands or regions, consent, access policies, and a consumption meter that is always running.

## Harmonization is where programs are won or lost

If I had to pick the stage where Data 360 programs actually fail, it's harmonization, and it's rarely for technical reasons.

Mapping a field is easy. Agreeing on what the field means is not. On the large programs I've led, the hardest conversations were seldom about which feature to use. They were about which system's version of an account was the true one, and who had the authority to decide. A data model object can't settle that for you. It makes the disagreement visible, which is useful if someone owns the decision and painful if nobody does.

So I treat the common model as a governance artifact first and a technical artifact second. Before a single stream is mapped, I want a short, signed-off list: what counts as a customer, what counts as an account, which source is authoritative for each attribute, and who arbitrates when two sources conflict. It's an unglamorous document. It saves months.

## Identity resolution is a business decision first

Identity resolution looks like a matching algorithm, and technically it is. Match rules can be exact, exact normalized or fuzzy, and they run on identifiers such as email, phone, name, address, party identifiers and keys you bring yourself. But every rule is also a decision about risk.

Match too loosely and you merge two different people, or two companies that share a billing address or a switchboard number, and an agent confidently tells one of them about the other's order. Match too tightly and the same customer exists five times, each record holding a fifth of the story. Neither error announces itself. Both show up later as bad segments, wrong answers and a loss of trust that is hard to win back.

In B2B and manufacturing the problem is harder than in consumer retail, because the unit that matters is usually the company, not the individual, and one real-world company can appear as a dozen sold-to, ship-to and bill-to records across ERP and CRM. Data 360 can resolve accounts as well as individuals, and in a manufacturing program I'd expect the account rules to carry more weight than the individual ones.

My practice is simple. Start with deterministic rules on identifiers you trust. Add fuzzy matching only where you can measure its error rate on a sample the business has reviewed. And keep the reconciliation rules (source priority, most recent, most frequent) written down next to the reason for each one, because someone will ask.

## Zero copy: when to leave the data where it lives

Most enterprises I work with already have a serious data platform, often Snowflake or Databricks, with a team that owns it. The instinct to copy all of that into Salesforce is understandable and usually wrong.

Zero copy lets Data 360 work with data where it already lives instead of ingesting it. My rule of thumb:

| Leave it where it lives | Bring it in |
|---|---|
| Large, slow-moving history owned by another team | Identifiers needed for identity resolution |
| Used for insights and segmentation, not per-record decisions | Data that has to trigger something in near real time |
| Already governed and modeled in the lake | Data an agent needs at low latency to answer a customer |
| Copying it would create a second source of truth | Sources with no warehouse behind them |

The trade-off to name early is cost. Live query federation against a warehouse such as Snowflake, Databricks, BigQuery or Redshift still draws on Data 360 consumption and also runs on the warehouse's compute, so there are two bills owned by two different teams. File federation over open table formats such as Iceberg shifts that balance. Either way, someone should model the cost on purpose. Dreamforce widened the options again, adding more AWS sources that are available now and more Google BigQuery connectivity due this fall.

This is also where the relationship with the data team becomes either a partnership or a turf war. Zero copy makes it a partnership: their platform stays the system of record for analytics, and Salesforce becomes the place where that data gets acted on.

## Grounding agents is the part everyone wants to skip

Nearly every executive conversation I've had this year eventually reaches agents. The demos are compelling. What the demos don't show is that an agent is only as good as what it's allowed to know, at the moment it needs to know it.

That's the real job Data 360 does for agents, and Dreamforce made it explicit. Structured context comes from unified profiles and data graphs, which pre-assemble the related records an agent needs so it isn't stitching them together mid-conversation. Unstructured context, such as manuals, policies, contracts and past cases, comes through search indexes and retrievers that make documents searchable by meaning. The Agent Context Engine is Salesforce's move to assemble all of that, with authorization applied, before the agent ever sees it.

Headless changes who is doing the reading. With Headless Data 360 and AIforce, the agent may not be inside Salesforce at all. A seller asking about an account through Claudeforce grounds on the same Data 360 profile as an Agentforce subagent in the service console. If that profile is wrong, both of them are wrong, in two different places, in front of two different people.

I've built retrieval systems outside Salesforce, including semantic search across a few million vectors for a nonprofit platform I run, and the lesson carries over directly: retrieval quality is a data problem before it's a model problem. Chunking, metadata, freshness and access control decide whether the answer is right far more than the choice of model does. An agent that can see stale inventory, or a contract it shouldn't have access to, doesn't have an AI problem. It has a data governance problem that happens to talk.

So my sequence doesn't change: harmonize, resolve identity, set access and consent, curate the retrieval sources, and only then build the first subagent or open the data to an outside surface.

## What this looks like for a manufacturer

Manufacturing is a good test of all of this, because the data is spread across more systems than almost anywhere else.

Orders and sales agreements live in the ERP. Accounts and opportunities live in Sales Cloud. Dealers and distributors have their own systems and their own identifiers. Warranty claims and service cases sit somewhere else again. Connected products send telemetry that nobody has tied to a customer record. Each system is good at its own job, and none of them can answer a simple question on its own: which of our largest accounts has rising warranty claims on a product line they're about to reorder?

Data 360 can answer that question, but not by boiling the ocean. The programs that work start with one use case that matters to someone with a budget, such as service-driven retention, forecast accuracy on sales agreements or dealer performance, and build only the ingestion, harmonization and identity resolution that use case needs. The second use case is then cheaper, because the foundation is already in place. The programs that stall try to unify everything first and deliver value later.

Headless makes the payoff bigger. Once that account view exists, a sales leader can ask for it in Claude, a service manager can see it in Lightning, and a dealer-facing agent can use it over MCP, without anyone building three separate integrations.

## Design for the bill

Data 360 pricing changed again this year. Since March it has run on Flex Credits alongside per-profile editions, and Salesforce's pricing page now advertises free batch ingestion, while streaming and most of the downstream processing still consume. The details will keep moving, so I won't quote figures that may be out of date by the time you read this.

The principle is stable. Streaming, transforms, unification, insights, segmentation, queries and activation all consume, and a design choice made casually in week two can set the run rate in year two. In practice that means estimating consumption as part of the architecture, not after go-live. It means choosing batch over streaming unless something genuinely needs real time, preferring incremental loads, scheduling calculated insights at the cadence the business actually uses, and reviewing consumption monthly with the same seriousness as a cloud bill. Headless adds one more line to plan for, because every outside agent reading the data is another consumer. The clients who end up happiest with Data 360 are the ones who were told the truth about cost at the start.

## What I'd tell a team starting a Data 360 program

Pick one use case with a named business owner and a measurable outcome. Write down what a customer and an account mean before mapping anything. Decide, source by source, whether data is federated or ingested, and record why. Start identity resolution conservative and loosen it only with evidence. Treat consent and access as part of the model, not a later security review. Decide early which surfaces will read the data, whether that's Agentforce inside Salesforce, Claude or Slack through AIforce, or your own agents over MCP, and hold all of them to the same access rules. Estimate consumption up front. And don't let anyone build an agent until the data it grounds on has been harmonized, resolved and governed.

None of that is new advice in spirit. It's what we've always said about data warehouses and master data. What has changed is the stakes. When the consumer of the data was a dashboard, a bad join produced a wrong chart. When the consumer is an agent talking to a customer, in Claude or Slack or your own app, it produces a wrong answer, in your company's voice, at scale.

That's why I sat this exam two weeks after the last one. The architecture is only as good as the data under it, and I wanted to be certain I can build both.

## Appendix: glossary

The terms used above, spelled out.

| Term | Full name | What it is |
|---|---|---|
| **Data 360** | Salesforce Data 360 | Salesforce's data platform, formerly Data Cloud, renamed at Dreamforce in October 2025 as the data layer of Agentforce 360. |
| **AIforce** | AIforce | Salesforce's layer, announced at Dreamforce 2026, that brings Salesforce data, workflows and logic to the surfaces where people and agents work, starting with Claude, Slack and Lightning. |
| **Claudeforce** | Claudeforce | The Salesforce and Anthropic partnership that puts Salesforce inside Claude. In beta for all customers since Dreamforce 2026. |
| **Slackforce** | Slackforce | The AIforce surface that brings Salesforce into Slack. |
| **Agentforce Coworker** | Agentforce Coworker | The AIforce surface in Lightning, available now. |
| **Headless Toolkit** | Headless Toolkit (introduced as Headless 360) | Salesforce's open architecture that exposes every platform capability as an API, MCP tool or CLI command. Introduced at TDX in April 2026. |
| **Headless Data 360** | Headless Data 360 | Exposes more than 200 Data 360 APIs to AI agents over MCP. Announced August 2026. |
| **MCP** | Model Context Protocol | An open standard for connecting AI agents to tools and data sources. |
| **Agentforce** | Salesforce Agentforce | Salesforce's platform for building and running AI agents. |
| **Subagent** | Subagent | A unit of agent behavior for a specific job in Agentforce. Called a topic until April 2026. |
| **Atlas Reasoning Engine** | Atlas Reasoning Engine | The reasoning engine behind Agentforce agents. |
| **Koa** | Koa | Salesforce's CRM reasoning model, built on NVIDIA Nemotron. In pilot, with general availability expected in winter 2026. |
| **Agent Context Engine** | Agent Context Engine (ACE) | A Data 360 capability that assembles governed, authorized context for agents from structured and unstructured sources. Announced at Dreamforce 2026. |
| **Trusted Enterprise AI Harness** | Trusted Enterprise AI Harness | Salesforce's architecture for trusted context, agency, action, governance, security and models across the enterprise, including the AI Control Plane. |
| **MuleSoft Agent Fabric** | MuleSoft Agent Fabric | MuleSoft's layer for discovering, governing and orchestrating AI agents across systems. |
| **Data stream** | Data stream | A configured feed that brings data from a source into Data 360. |
| **DLO** | Data Lake Object | Where ingested data lands, in essentially the shape the source sent it. |
| **DMO** | Data Model Object | An object in the common, harmonized data model that raw data is mapped onto. |
| **Harmonization** | Data harmonization | Mapping source data onto a shared model so that different systems mean the same thing. |
| **Identity resolution** | Identity resolution | The process that decides which records represent the same person or company and merges them into a unified profile. |
| **Match rules** | Match rules | The criteria (exact, exact normalized or fuzzy) that decide two records are the same entity. |
| **Reconciliation rules** | Reconciliation rules | The logic that decides which value wins when matched records disagree. |
| **Unified profile** | Unified Individual or Unified Account | The single, resolved record for a person or a company. |
| **Calculated insight** | Calculated insight | A metric computed over unified data, such as lifetime value or a warranty claims rate. |
| **Streaming insight** | Streaming insight | A metric computed in near real time on incoming events. |
| **Data action** | Data action | An event Data 360 sends when conditions are met, used to trigger flows or external systems. |
| **Data graph** | Data graph | A pre-assembled view of related records that agents and applications can read quickly. |
| **Search index, retriever** | Search index, retriever | The components that make unstructured content searchable by meaning, so agents can ground their answers in it. |
| **Zero copy** | Zero-copy data federation | Working with data where it lives, for example in Snowflake or Databricks, instead of copying it in. |
| **Data space** | Data space | A logical partition of Data 360 data, for example by brand or region, with its own access. |
| **Flex Credits** | Flex Credits | Salesforce's consumption currency, used for Data 360 since March 2026. |
| **ERP** | Enterprise Resource Planning | The back-office system of record, such as SAP or Oracle, for orders, inventory and finance. |

*If you're planning a Data 360 or agent program and want to compare notes, I'm easy to reach. See the [contact section](/#contact).*
