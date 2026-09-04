# Stage 7 Institutional Validation — C-ESD

Date: 2026-09-04

Purpose: validate institutional plausibility of the frozen C-ESD primitives without converting analogies into facts.

## Evidence labels

- `ESTABLISHED`: directly supported by primary legal/regulatory text.
- `SUGGESTIVE`: primary evidence supports a close analogue but not the full modeled mechanism.
- `UNVERIFIED`: model prediction not established by the audited primary source.
- `CONTRADICTED`: primary evidence conflicts with the modeled interpretation.

## Setting A — EU electric-vehicle charging interoperability

Primary sources:

- Regulation (EU) 2023/1804 on the deployment of alternative fuels infrastructure (AFIR), especially Annex II and Article 21.
- European Commission, Q&A on Regulation (EU) 2023/1804 and common technical specifications.

Findings:

1. **Government/regulatory policy can impose interoperability-relevant technical specifications — ESTABLISHED.**
   AFIR requires common technical specifications for interoperability and specifies connector standards such as Type 2 / Combo 2 for relevant charging points.

2. **Interoperability policy can target a specific interface dimension rather than every product characteristic — ESTABLISHED.**
   The Commission Q&A states that the cited charging standard is mandated for technical elements relevant to interoperability, not every non-interoperability aspect such as safety.

3. **Compatibility has a network/infrastructure reach interpretation — SUGGESTIVE.**
   The regulation is explicitly designed around interoperable charging/refuelling infrastructure. This supports the model's network-access interpretation, but the legal text is not an empirical estimate of the network-effect coefficient `v`.

4. **Vehicle manufacturers strategically increase differentiation on other product dimensions after connector harmonization — UNVERIFIED.**
   This is a C-ESD empirical prediction, not an observed fact established by AFIR.

5. **Regional-bloc integration can make an outsider interface relatively more differentiated — SUGGESTIVE.**
   A common regional interface can create a bloc boundary relative to incompatible external systems, but the exact Stage-3 affine map `tau_cross=t_bar+(s_C+s_D)/2` is a model normalization, not a legal fact.

Overall mapping: **strong institutional fit for the policy-controlled interface-friction primitive; partial fit for network reach; strategic repositioning remains a testable prediction.**

## Setting B — EU Digital Markets Act messaging interoperability

Primary source:

- Regulation (EU) 2022/1925 (Digital Markets Act), Article 7.

Findings:

1. **A regulator can require interoperability through technical interfaces or similar technical solutions — ESTABLISHED.**
   Article 7 requires designated gatekeepers providing number-independent interpersonal communications services to make basic functionalities interoperable with requesting providers by providing necessary technical interfaces or similar solutions.

2. **Interoperability can be granular in functionality rather than binary — ESTABLISHED / SUGGESTIVE.**
   Article 7 specifies basic functionalities and allows requests covering some or all listed functionality. This validates the general idea of an interoperability-depth margin, although it does not instantiate the C-ESD scalar `s_C`.

3. **Network reach matters in messaging markets — SUGGESTIVE.**
   Interoperability connects users across services by construction, but the legal text does not by itself estimate or prove the economic network externality used in the model.

4. **Providers respond to mandated interoperability by changing other service characteristics — UNVERIFIED in the primary source.**
   The model predicts such repositioning; the DMA text does not establish it as an observed response.

5. **The exact government-coalition structure IS/SU/SW maps literally to the DMA — CONTRADICTED if stated literally.**
   The DMA is an EU regulatory regime, not a three-country standards-coalition formation game. It is usable only as a distinct institutional analogue for the interoperability-policy/product-response mechanism.

Overall mapping: **strong support for a policy-controlled technical interoperability margin in a digital network service; weak support for the coalition interpretation.**

## Optional physical-product cross-check — EU common charger

Primary source:

- Directive (EU) 2022/2380 amending the Radio Equipment Directive.

The Directive requires covered wired-chargeable devices to use a USB Type-C receptacle and, for relevant higher-power charging, USB Power Delivery while permitting additional charging protocols so long as full USB-PD functionality is preserved.

Classification:

- common interface mandate: `ESTABLISHED`;
- standardization of one interface dimension while other product dimensions remain open: `ESTABLISHED / SUGGESTIVE`;
- post-standardization strategic re-differentiation by device makers: `UNVERIFIED`.

## Generality conclusion

The C-ESD mechanism is not institution-specific provided four economic objects exist:

1. a policy-controlled compatibility/interface margin;
2. network/access value from compatibility;
3. a separate horizontal characteristic on which firms can reposition;
4. decentralized national/regional objectives that value domestic producer rents differently from global welfare.

EV charging and digital messaging are genuinely different technological settings that contain the first two objects. The third object is plausible but empirically unverified in the audited primary sources. The fourth object is specific to international/regional policy applications and should not be claimed for the DMA analogue.

Therefore institutional validation is **sufficient for theoretical plausibility but not empirical confirmation of the strategic repositioning mechanism**.