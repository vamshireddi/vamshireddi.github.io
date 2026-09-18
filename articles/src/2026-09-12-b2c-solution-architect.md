---
title: The Customer Is the Architecture
subtitle: Why I sat the Salesforce B2C Solution Architect exam after 17 years on the platform, and what a multi-cloud, agent-first stack actually looks like in 2026
date: 2026-09-12 09:00
updated: 2026-09-18
toc: true
summary: I earned the Salesforce Certified B2C Solution Architect credential this week. The exam is less about any one cloud than about the decisions between them — Data 360 as the spine, headless commerce, Agentforce as a new interface, and integration as the thing that makes or breaks all of it. Here is how I think about that architecture, and what Dreamforce 2026 changed.
tags: [Salesforce, Architecture, Agentforce, Data 360, Commerce, AI]
cover: /articles/images/b2c-solution-architect-certificate.jpg
cover_alt: Salesforce Certified B2C Solution Architect certificate presented to Vamshi Krishna Reddy Bandaru, issued September 12, 2026, credential ID 8126907
---

I've held the Salesforce Systems Architect and Application Architect credentials for years, and I've been the design authority on programs where a single decision about the account model or the sharing model touched tens of thousands of users. So when people ask why I sat another architect exam this month, the honest answer is that the B2C Solution Architect credential tests the one thing the other two don't: **the space between the clouds.**

Systems Architect asks whether you can make one platform scale and stay secure. Application Architect asks whether you can build on it well. B2C Solution Architect asks whether you can stand in front of a retailer, a hotel group, or a consumer brand, understand their business, and design how Commerce, Marketing, Service, Loyalty, and Data 360 become *one* system for *one* customer — and how that system survives contact with an ERP, a point-of-sale, a payment provider, and now a fleet of AI agents. The exam weights it that way: architectural design at 23%, data models and management at 21%, integration at 19%, functional capabilities and business value at 19%, and discovery and customer success at 18%. Almost half of it is data and integration. That is exactly where B2C programs succeed or fail.

[Verify the credential](https://sforce.co/verifycerts) — Credential ID 8126907, issued September 12, 2026. Acronyms (SCAPI, SFRA, SLAS, and the rest) are spelled out in the [glossary at the end](#appendix-glossary).

## The picture I carry into every B2C conversation

![B2C reference architecture: experience surfaces, agent and API layer, engagement clouds, Data 360 spine, systems of record](/articles/images/b2c-reference-architecture.svg)

Five layers, and the order matters.

At the top are the **experience surfaces**, and there are more of them every quarter: a composable storefront, a native mobile app, WhatsApp and SMS, a voice agent, a store associate's console, and — new this year — other companies' AI assistants shopping on a customer's behalf. Ten years ago the storefront was the architecture. Today it's one client among many.

Below that sits the **agent and API layer**: the Commerce API and its identity service, Agentforce with its topics and actions, and MuleSoft with API-led connectivity and the Agent Fabric registry. This is the layer that decides whether adding a new surface is a two-week project or a two-quarter one.

Then the **engagement clouds** — Commerce, Marketing, Service, Loyalty, Experience Cloud — each excellent at its job, each with its own idea of who the customer is unless you stop it.

Which is why the fourth layer, **Data 360**, is the spine of the whole diagram. Unified profile, identity resolution, consent, calculated insights, and a semantic layer that agents can reason over. If a shopper abandons a cart on the app, opens a service case on the phone, and redeems loyalty points at a counter, there has to be exactly one record of that person, and every cloud and every agent has to read from it. Every B2C failure I've seen up close traces back to this layer being an afterthought.

At the bottom are the **systems of record and the ML estate** — ERP, inventory, POS or PMS, payments, the data lake, the models. They don't change often, and they shouldn't have to know about the layers above them.

## Headless is no longer a preference; it's a requirement

The old debate was SFRA versus headless — template-driven storefront versus React on top of APIs. That debate is over, and not because React won. It's because the number of front ends exploded. When a customer can start a purchase in a chat window, continue it through a voice agent, and finish it on a phone, the storefront can't own the business logic. The back end has to: catalog, pricing, inventory, cart, promotions, order management — exposed through the Commerce API and consumed by whatever surface the customer happens to be using.

Salesforce's own direction confirms it. The legacy commerce API was deprecated in April 2026; everything new is built on SCAPI, PWA Kit, and Managed Runtime, and the B2B side now runs fully headless with "two paths, one back end." The architectural consequence is that identity (SLAS), session context, and personalization signals have to be designed once at the API layer, not re-implemented per surface. That is a data-and-integration problem wearing a front-end costume.

## Agentforce changes what an interface is

Here's the shift that I think most architecture diagrams haven't caught up with: an AI agent is not a feature you add to a channel. It's a *new channel*, and increasingly it's a new *customer* — because the shopper's own assistant may be the one calling your APIs. Salesforce's numbers from the 2025 holiday season put AI-influenced online sales at roughly 20% of the total, and AI-referred traffic converting at eight times the rate of social traffic. Whether those figures hold everywhere or not, the direction is unambiguous.

That has three architectural implications I now design for by default. First, **grounding**: an agent is only as trustworthy as the data it can see, so Data 360 and Knowledge must be curated before the first topic is written. Second, **least privilege**: an agent acts *as* someone, and it must see only what that person is allowed to see — the same discipline we apply to Experience Cloud users, extended to a system that generates its own queries. Third, **human-in-the-loop by design**: I keep transactional actions deterministic (Flows, Apex, APIs) and let the model decide *which* action, never *how* to mutate data — and I build the escalation path to a human agent with full context before I build anything else. I'm as enthusiastic about agents as anyone; that's precisely why I'm strict about their boundaries.

## Where the AI/ML work actually lives

People assume the machine learning in a B2C stack is "the recommendations." It's broader and less glamorous. Identity resolution is a matching problem. Propensity and churn are supervised models that need a feature pipeline out of Data 360 and back into segmentation. Inventory-aware promotions are optimization. Agent quality is an evaluation problem — utterance sets, regression runs, containment and escalation rates. The architect's job is to know which of these wants a rule, which wants a classical model, and which genuinely needs a large language model, and to say so out loud in a room where the vendor pitch says "AI" for all of them.

That judgment is what I spent the last nine months sharpening in the [UT Austin McCombs AI & ML program](/articles/nine-months-as-a-student-again/). Pairing that with a multi-cloud Salesforce credential in the same month wasn't a coincidence. The most valuable person on a B2C program right now is the one who can hold both.

## What leadership looks like on a program like this

Multi-cloud programs don't fail on technology. They fail because the commerce team, the marketing team, and the service team each believe they own the customer, and nobody owns the decisions between them. The architect's leadership job is to make those decisions explicit, early, and reversible where possible. In practice that means: run discovery across all the business owners before designing anything, publish a decision log where each choice records the options that were rejected and why, get the data and identity model signed off before automation is built, and chair an architecture board that has the authority to say no to a stream that wants its own copy of the customer.

The B2C exam tests this in its own way — it's the reason "discovery and customer success" carries nearly a fifth of the weight. You can't architect what you haven't understood, and you can't lead a program whose stakeholders haven't agreed on what the customer is.

## What I'd tell a team starting a B2C program in 2026

Design the identity and consent model first, because everything grounds on it. Treat the storefront as one client of the API layer, not the center of the universe. Assume there will be surfaces you haven't planned for, including agents you don't control. Put Data 360 in the architecture on day one, not as a phase-two analytics project. Be specific about where machine learning earns its keep. And put a human in the loop before you put an agent in front of a customer.

## Postscript — what Dreamforce 2026 changed (September 18)

I wrote the sections above on the day the credential was issued. Three days later, Dreamforce made the direction even clearer. Salesforce introduced **AIforce** — described on stage as a productized step above "Headless 360," with Claude, Slack, and the Lightning interface as the first three surfaces; **Koa**, a CRM-specialized model built with NVIDIA; a consolidated "harness" that names Data 360, MuleSoft Agent Fabric, Tableau semantics, and governance as the foundation for agents; and a set of pre-built agents for support, shopping, sales, and finance. It also quietly walked back the spring's product renames — Sales Cloud, Service Cloud, Marketing Cloud, and Commerce Cloud are Sales Cloud, Service Cloud, Marketing Cloud, and Commerce Cloud again.

None of that changes the diagram above; it confirms it. The surfaces multiply, the data spine gets more important, and the value moves to whoever can design the layer in between.

## Appendix — glossary

The acronyms used above, spelled out.

| Term | Full name | What it is |
|---|---|---|
| **SCAPI** | Salesforce Commerce API | The REST API layer for B2C Commerce Cloud — Shopper APIs for the customer-facing side, Admin APIs for merchants. Replaces OCAPI. |
| **OCAPI** | Open Commerce API | The older Commerce Cloud REST API, deprecated April 2026. |
| **SFRA** | Storefront Reference Architecture | Salesforce's server-rendered, template-based B2C storefront that teams customize with cartridges. |
| **PWA Kit** | Progressive Web App Kit | Salesforce's open-source React framework for building a headless storefront on SCAPI. |
| **MRT** | Managed Runtime | Salesforce-hosted environment where PWA Kit storefronts are deployed (dev/staging/production, CDN, logs). |
| **SLAS** | Shopper Login and API Access Service | The OAuth/OpenID identity service that issues shopper tokens for SCAPI calls; its hybrid mode lets SFRA and headless pages share one session. |
| **PKCE** | Proof Key for Code Exchange | The OAuth extension SLAS uses so browsers and mobile apps can log in securely without a client secret. |
| **JWT** | JSON Web Token | The signed token format SLAS issues for shopper sessions. |
| **OMS** | Order Management System | Salesforce Order Management — orders after checkout: fulfillment, returns, service. |
| **POS** | Point of Sale | The in-store register and checkout system. |
| **PMS** | Property Management System | The hotel operations system (reservations, rooms, folios), relevant in hospitality designs. |
| **ERP** | Enterprise Resource Planning | The back-office system of record (SAP, Oracle) for inventory, pricing, and finance. |
| **CDP** | Customer Data Platform | The product category Data 360 belongs to: unifies customer data across systems into one profile. |
| **Data 360** | — | Salesforce's current name for Data Cloud (renamed at Dreamforce, October 2025). |
| **API-led connectivity** | — | MuleSoft's pattern of layering System, Process, and Experience APIs so back ends are reused rather than wired point-to-point. |
| **Agent Fabric** | — | MuleSoft's registry and governance layer for AI agents — discover, connect, and control agents across systems. |
| **SSR** | Server-Side Rendering | Pages rendered on the server (as PWA Kit does) so they load fast and search engines can index them. |
| **IdP** | Identity Provider | The system that authenticates users — Okta, Entra ID, or a customer login service. |
| **GA** | General Availability | A product or feature released to all customers, as opposed to beta or pilot. |

*If you're planning a B2C or agent program and want to compare notes on the architecture, I'm easy to reach — see the [contact section](/#contact).*
