# Revisi Menyeluruh — *Life Cycle Assessment of Small-Scale Tofu Production in Semarang City* (ver2)

> **Catatan untuk penulis.** Semua angka diambil **langsung dari Tabel 2, 3, dan 4 yang baru** (hasil running ulang SimaPro 10.3). Tidak ada angka yang dikarang. Nilai impact (Tabel 2) dan normalisasi (Tabel 4) dinyatakan **per functional unit = 1 kg tofu**; angka inventory (mis. 800 kg firewood, 10.434 L whey) hanya dirujuk per batch saat menjelaskan sumber data. **Tidak ada nilai tabel/gambar yang diubah.**
>
> **Klarifikasi penulis yang sudah saya terapkan:**
> 1. **Wastewater dan whey = *emission to water*** (kesalahan pelabelan di Tabel 1). Interpretasi EP/FAET pada coagulation kini dikaitkan ke whey. → lihat catatan koreksi Tabel 1.
> 2. **GWP disesuaikan** agar tidak kontradiksi: CO₂ firewood diperlakukan biogenik (carbon-neutral), sehingga GWP boiling digerakkan oleh CH₄, N₂O, dan rantai pasok hulu firewood.
> 3. **Tanpa alokasi** karena produk tunggal (tofu); whey dan okara = limbah (bukan co-product).
>
> **Perubahan besar vs narasi lama:** hotspot dominan bukan *washing*, melainkan **boiling** (GWP, water scarcity) dan **coagulation** (ODP, AP; serta EP/FAET via whey), dengan **grinding** menonjol pada FAET (listrik). Setelah normalisasi **GWP tertinggi** (bukan FAET). Total AWARE **569 m³ world eq** (bukan 515).

---

## 1. Revised Introduction

*(Perubahan: menambahkan keseimbangan narasi energi/firewood pada paragraf 1, tanpa menambah/menggeser nomor referensi. Paragraf 2–3 tetap.)*

Tofu (tahu) is a staple plant-based protein in Indonesia, consumed at roughly 0.16 kg per capita per week and produced largely by household-scale and small and medium-sized enterprises (SMEs) [1]. This sustained demand generates large volumes of high-strength organic wastewater rich in dissolved proteins, suspended solids, and soybean residues, which are frequently discharged with little or no treatment [2, 3]. Such effluents are a recognized driver of freshwater degradation: the food-processing sector is among the leading contributors to surface-water pollution in Indonesia, with untreated organic discharge elevating biochemical oxygen demand (BOD) and chemical oxygen demand (COD) in receiving rivers well beyond regulatory limits [4]. In dense urban settings such as Semarang City, where tofu SMEs typically operate close to riverine systems with limited treatment infrastructure, the ecological significance of process-level liquid waste is amplified. **Beyond liquid effluents, however, tofu processing is also energy-intensive, depending heavily on firewood combustion at the boiling stage; a balanced environmental assessment must therefore weigh both water-related and energy-related burdens rather than either alone.**

Life Cycle Assessment (LCA), standardized under the ISO 14040 and ISO 14044 framework, is a rigorous approach for quantifying environmental burdens across a defined production system and for identifying the stages that disproportionately drive impacts [5]. LCA has been applied to Indonesian tofu production, but with recurring methodological gaps. Rosyidah et al. [6] and Nugroho et al. [7] focused mainly on greenhouse-gas emissions and identified firewood-fired boiling as the dominant emission source; Sari et al. [8] applied CML-IA in a cradle-to-gate study but did not resolve freshwater ecotoxicity at the stage level; and Hartini et al. [9] coupled LCA with life cycle costing and confirmed freshwater ecotoxicity and eutrophication as leading categories. However, none of these gate-to-gate Indonesian studies combined the CML-IA Baseline method with a dedicated, stage-resolved water-scarcity assessment [10]. Critically, the AWARE water-scarcity method has not been applied to Indonesian tofu production, and no LCA has been reported for Semarang City, where urban water dynamics may yield burden profiles distinct from rural production sites [11].

This study addresses these gaps by conducting a gate-to-gate LCA of SME-scale tofu production in Semarang City with four objectives: (1) to quantify impacts across five CML-IA Baseline midpoint categories using SimaPro 10.3; (2) to assess water scarcity with the AWARE method; (3) to characterize stage-level material and energy flows following standardized life cycle inventory guidance; and (4) to identify environmental hotspots and propose targeted, source-oriented improvement strategies for urban tofu SMEs, consistent with cleaner-production and circular-economy principles.

---

## 2. Revised Methods — *klarifikasi terarah (nilai tidak diubah)*

> Sesuai instruksi, Methods **tidak dirombak**. Hanya tiga klarifikasi yang ditambahkan agar interpretasi hasil tidak bertentangan dengan model. Kalimat tambahan ditandai **tebal**.

**2.1 Goal and scope definition (tambahan di akhir paragraf pertama).**
The functional unit was established as 1 kg of tofu produced, consistent with comparable LCA studies of tofu and soy-based food processing [8]. All inventory data were initially collected on a per-batch basis representing one complete production day, with 1,400 kg of soybeans as raw material input yielding 3,681 kg of tofu. **Because tofu is the sole marketable product of the system, no allocation was applied; the whey and okara generated during processing were treated as waste outputs rather than co-products, with whey and process wastewater modeled as emissions to the freshwater compartment.**

**2.2 Life Cycle Inventory Analysis (tambahan).**
**Process wastewater (from washing, soaking, and molding) and the whey separated during coagulation were modeled as emissions to water, carrying the organic and nutrient load (dissolved proteins, suspended solids, and nitrogen- and phosphorus-bearing compounds) released from the soybeans during processing. Okara and wood ash were treated as solid waste outputs.**

> **[Table 1 — koreksi pelabelan yang disarankan]** Pindahkan baris **"Wastewater"** dan **"Whey"** dari kelompok *"Output product / Output material"* ke kelompok **"Emission (to water)"** agar sesuai dengan elementary flow yang dimodelkan di SimaPro. **Nilai numerik tidak berubah**, hanya pengelompokan barisnya.

**2.3 Impact Assessment (tambahan singkat soal CO₂ biogenik).**
The CML-IA Baseline method was applied in SimaPro 10.3 across five impact categories (GWP, ODP, FAET, AP, EP), and water scarcity was additionally assessed using the AWARE method [11]. **Consistent with standard LCA practice for biomass fuels, the CO₂ released from firewood combustion was treated as biogenic and carbon-neutral; consequently, the global-warming contribution of the boiling stage derives from the non-CO₂ combustion gases (CH₄ and N₂O) and from the fossil emissions embedded in the upstream firewood supply chain rather than from the combustion CO₂ itself.**

> **[CHECK DATA]** Mohon konfirmasi setelan *biogenic carbon* pada SimaPro 10.3 sesuai kalimat di atas (ini yang menjelaskan mengapa GWP terkarakterisasi < total CO₂ yang diemisikan).

---

## 3. Revised Abstract

The tofu industry is a vital food-processing sector in Indonesia, but its production requires high water and energy inputs and generates organic wastewater. This study evaluated the potential environmental impacts of small-scale tofu production in Semarang City using a gate-to-gate Life Cycle Assessment with a functional unit of 1 kg of tofu. The system boundary covered washing, soaking, grinding, boiling, filtration, coagulation, and molding and packing. Impact assessment was performed in SimaPro 10.3 using the CML-IA Baseline method for Global Warming Potential (GWP), Ozone Layer Depletion (ODP), Freshwater Aquatic Ecotoxicity (FAET), Acidification (AP), and Eutrophication (EP), and water scarcity was additionally assessed with the AWARE method. The boiling and coagulation stages were the dominant environmental hotspots. Per kilogram of tofu, total GWP was 1.84 × 10⁻¹ kg CO₂ eq and was governed by firewood use at the boiling stage (88.0%), while FAET (1.30 × 10⁻² kg 1,4-DB eq) was distributed across boiling (34.7%), coagulation (29.5%), and grinding (24.2%). ODP (2.53 × 10⁻¹⁰ kg CFC-11 eq) and AP (1.27 × 10⁻⁴ kg SO₂ eq) were led by the coagulation stage, whereas EP (1.75 × 10⁻⁴ kg PO₄³⁻ eq) was driven by boiling and by the whey discharged as emission to water at coagulation. After normalization, GWP showed the highest value (3.66 × 10⁻¹⁴), followed by FAET (2.50 × 10⁻¹⁴) and EP (1.32 × 10⁻¹⁴), indicating that firewood-related climate impact and freshwater ecotoxicity are the foremost environmental priorities. The AWARE assessment yielded a total water-scarcity impact of 569 m³ world eq, dominated by the boiling stage (51.7%) through the embedded water footprint of firewood. Practical improvement strategies include organic wastewater treatment with biogas recovery, water reuse, fuel substitution, and improved thermal efficiency. This study provides process-level evidence to support cleaner production in small-scale urban tofu industries in Semarang City.

**Keywords:** Life Cycle Assessment; Tofu Production; CML-IA Baseline; AWARE; Environmental Hotspot.

---

## 4. Revised Results and Discussion

### 3.1 Potential Environmental Impact of Tofu Production

The LCIA results per production stage are summarized in Table 2 and expressed per functional unit (1 kg of tofu). A notable feature is the absence of impact values for the filtration stage across all categories. This is attributable to the absence of explicit energy inputs or additional material flows for that stage: filtration operates as a passive mechanical separation step without recorded electricity consumption, so SimaPro 10.3 did not generate characterization values for it. This is consistent with the inventory in Table 1, where filtration is limited to the passage of boiled slurry and the separation of soy milk from okara residue.

Across the five categories, two stages emerge as recurrent hotspots: **boiling**, driven by firewood combustion, and **coagulation**, associated with the organic- and nutrient-rich whey discharged as emission to water, with **grinding** contributing appreciably to ecotoxicity through its electricity demand. The washing stage, by contrast, is a minor contributor (0.1–4.3%) in every CML-IA category.

**a. Global Warming Potential (GWP).** Total GWP is 1.84 × 10⁻¹ kg CO₂ eq per kg tofu. The boiling stage is by far the largest contributor at 1.62 × 10⁻¹ kg CO₂ eq (88.0%), followed by coagulation (8.3%) and grinding (2.5%). Boiling's dominance is driven by firewood use: because the CO₂ released from firewood combustion is treated as biogenic and carbon-neutral, the stage's characterized GWP is governed by the non-CO₂ combustion gases CH₄ (0.0499 kg) and N₂O (0.3744 kg) per batch — both substantially more potent than CO₂ — together with the fossil emissions embedded in the upstream firewood supply chain (procurement, processing, and transport). This finding is consistent with comparative LCA studies of wood-fired tofu production in Indonesia, where boiling was repeatedly identified as the primary emission source [6, 7]. The smaller coagulation contribution may be attributed to the upstream supply chain of the coagulant input.

**b. Ozone Layer Depletion (ODP).** Total ODP is 2.53 × 10⁻¹⁰ kg CFC-11 eq, led by coagulation (53.8%) and boiling (27.2%), with molding and packing contributing 13.9%. Because none of these stages involves halogenated substances directly, the burden is allocated within the LCA framework to trace ozone-depleting and nitrogen-bearing substances embedded in the upstream supply chains of the coagulant, firewood, and packaging materials [5]. Given its negligible normalized value (Section 3.3), ODP is not an environmental priority for this system, and this pattern is reported for completeness rather than as a management target.

**c. Freshwater Aquatic Ecotoxicity (FAET).** Total FAET is 1.30 × 10⁻² kg 1,4-DB eq and is the most evenly distributed category, with boiling (34.7%), coagulation (29.5%), and grinding (24.2%) together accounting for about 88% of the total. The grinding contribution is primarily associated with its electricity demand (17 kWh per batch, the largest of any stage), as freshwater ecotoxicity in the CML-IA method is strongly influenced by heavy-metal releases attributed to grid-electricity generation. The coagulation contribution may be attributed to the whey discharged as emission to water — the largest liquid output of the system (10,434 L per batch) — and to the upstream supply chain of the coagulant input, whereas the boiling contribution reflects the firewood supply chain and the aquatic deposition of combustion-derived emissions [6]. This distributed ecotoxicity profile is consistent with prior Indonesian tofu LCA studies that rank freshwater ecotoxicity among the most significant categories [9].

**d. Acidification (AP).** Total AP is 1.27 × 10⁻⁴ kg SO₂ eq, led by coagulation (48.4%) and boiling (36.4%), with grinding contributing 9.3%. The boiling burden derives from SO₂ and NOₓ released during firewood combustion, the principal acidification precursors, while the coagulation contribution is primarily associated with the upstream energy and material supply chains of the coagulant input rather than with the whey itself, since acidification is governed by airborne rather than waterborne emissions [5]. Firewood-derived acidifying emissions may form acid deposition with potential consequences for soil and receiving waters near the facility.

**e. Eutrophication (EP).** Total EP is 1.75 × 10⁻⁴ kg PO₄³⁻ eq, driven mainly by boiling (48.1%) and coagulation (38.9%). The coagulation contribution is primarily associated with the nutrient-rich whey discharged as emission to water, which carries nitrogen- and phosphorus-bearing compounds released during protein coagulation; if discharged untreated, such effluents can trigger algal proliferation, dissolved-oxygen depletion, and disruption of aquatic ecosystems [2]. The boiling contribution reflects the atmospheric deposition of combustion-derived NOₓ, while grinding adds a further 9.4% through its electricity demand.

### 3.2 Water Use Assessment

Water use was assessed with the AWARE method, which expresses the volume of water deprived from downstream users per unit consumed at a given location. The total water-scarcity impact of the production system is 569 m³ world eq (Table 3). Consistent with the GWP pattern, the boiling stage is the dominant contributor at 294 m³ world eq (51.7%). This reflects the AWARE method's sensitivity to upstream supply-chain water consumption: firewood procurement, processing, and distribution embed substantial water use that is allocated back to boiling, elevating its scarcity value beyond what direct water consumption alone would suggest. Grinding contributes the second-largest share (101 m³ world eq, 17.8%), consistent with the continuous water addition required to achieve appropriate slurry consistency. Washing (65.3 m³ world eq, 11.5%) and soaking (63 m³ world eq, 11.1%) follow, while coagulation (6.7%) and molding and packing (1.3%) are minor. The comparatively modest scarcity value of washing, despite its substantial direct water use, illustrates that water-scarcity characterization is governed not solely by withdrawn volume but by regional water availability and the embedded water footprint of upstream inputs [11].

### 3.3 Normalization

Normalization was performed using the CML-IA Baseline reference values to place all categories on a common dimensionless scale (Table 4). The results identify GWP as the dominant impact category (3.66 × 10⁻¹⁴), followed closely by FAET (2.50 × 10⁻¹⁴) and then EP (1.32 × 10⁻¹⁴); AP (4.51 × 10⁻¹⁵) and ODP (2.83 × 10⁻¹⁸) are comparatively minor. The normalized ranking mirrors the absolute ranking and indicates that the system's two most consequential pressures are the climate burden of firewood combustion at boiling and the freshwater-ecotoxicity burden distributed across boiling, coagulation, and grinding. This convergence is significant: it suggests that interventions at the boiling stage can simultaneously relieve the highest-ranked category (GWP) and a leading mid-ranked category (FAET), while organic liquid-waste management — particularly of the coagulation whey — addresses the remaining freshwater-related burdens (FAET and EP). AP and ODP contribute relatively minor normalized values and are therefore not the primary environmental priorities for this system.

### 3.4 Hotspot Identification and Improvement Strategies

The integrated analysis of LCIA and normalization results identifies two primary hotspots: (i) **firewood combustion during boiling**, which dominates GWP and water scarcity and contributes substantially to EP, AP, and FAET; and (ii) **organic liquid-waste generation, principally the coagulation whey stream together with washing and soaking effluents**, which drives EP and contributes substantially to FAET. The electricity demand of grinding is a secondary driver of freshwater ecotoxicity. The recommended, evidence-based improvement strategies are summarized in Table 5.

For the first hotspot, boiling contributes disproportionately to GWP and water scarcity owing to its reliance on firewood: combustion of 800 kg per batch releases the greenhouse gases CH₄ (0.0499 kg) and N₂O (0.3744 kg) alongside biogenic CO₂, and embeds a substantial upstream water footprint. Transitioning to cleaner energy, such as LPG or biomethane recovered from on-site biodigesters, would directly reduce these emissions while lowering the upstream water footprint of the firewood supply chain [14]. Adopting improved-combustion or thermally insulated boiling systems, together with waste-heat recovery to pre-heat process water, would further reduce specific fuel consumption.

For the second hotspot, the high-BOD/COD, nutrient-rich effluents — especially the whey generated during coagulation (10,434 L per batch), the largest liquid output of the system and the principal eutrophication driver at this stage — pose significant risks to receiving ecosystems if discharged untreated. Anaerobic treatment (e.g., biodigesters or integrated biogas wastewater units) is technically appropriate for SME-scale operations because it reduces organic loading while recovering biogas as an energy resource, simultaneously lowering FAET and EP (through effluent-load reduction) and GWP (through fuel displacement) [2]. Complementary measures include counter-current water recycling within washing and soaking to cut both water consumption and effluent generation [13], and valorization of whey as a protein-rich feed or fermentation substrate to divert high-nutrient streams away from discharge. Overall, the LCA evidence demonstrates that interventions targeting energy efficiency and liquid-waste management at the source yield substantially greater environmental benefit than conventional end-of-pipe approaches.

---

## 5. Revised Conclusion

This study applied a gate-to-gate Life Cycle Assessment to evaluate the environmental impacts of small-scale tofu production in Semarang City using the CML-IA Baseline and AWARE methods, with a functional unit of 1 kg of tofu. Tofu production generated impacts in all assessed categories, with totals of 1.84 × 10⁻¹ kg CO₂ eq (GWP), 2.53 × 10⁻¹⁰ kg CFC-11 eq (ODP), 1.30 × 10⁻² kg 1,4-DB eq (FAET), 1.27 × 10⁻⁴ kg SO₂ eq (AP), and 1.75 × 10⁻⁴ kg PO₄³⁻ eq (EP). The boiling and coagulation stages were the principal hotspots: boiling dominated GWP (88.0%) and water scarcity (51.7%) through firewood combustion and its embedded water demand, while coagulation led ODP and AP and, together with boiling and grinding, governed freshwater ecotoxicity and eutrophication, largely through the whey discharged as emission to water. Normalization identified GWP as the most significant category (3.66 × 10⁻¹⁴), followed by FAET (2.50 × 10⁻¹⁴) and EP (1.32 × 10⁻¹⁴), and the AWARE assessment yielded a total water-scarcity impact of 569 m³ world eq, dominated by boiling.

These findings indicate that the climate burden of firewood combustion and the freshwater impacts of organic liquid waste are the most acute environmental concerns of urban tofu SMEs, and that environmental management should prioritize boiling-stage energy efficiency together with organic liquid-waste treatment and water reuse. Practical, high-leverage measures include fuel substitution and improved thermal systems, anaerobic treatment with biogas recovery, and counter-current water recycling, all of which act upstream at the source rather than end-of-pipe. By providing the first stage-resolved, AWARE-supported LCA of tofu production in Semarang City, this study contributes process-level evidence to support cleaner production in urban food SMEs. Future research should extend the boundary toward cradle-to-grave and integrate life cycle costing to confirm the economic feasibility of the proposed interventions.

---

## 6. Citation and Reference Audit Table

**Ringkasan:** 14 referensi ([1]–[14]) → ≤ 15 (memenuhi batas). **Semua dalam rentang 2016–2026** dan **semua tersitasi** di teks. Penomoran sudah mengikuti urutan kemunculan pertama, sehingga **tidak ada renumbering**. Tidak ada referensi yang dihapus atau ditambahkan; tidak ada "Suggested reference" yang diperlukan.

| Ref lama | Ref baru | Masih digunakan? | Tahun | Dalam 2016–2026? | Catatan |
|---|---|---|---|---|---|
| [1] Badan Pusat Statistik | [1] | Ya (Intro) | 2026 | Ya | Data konsumsi; tetap. |
| [2] Seroja et al. | [2] | Ya (Intro, 3.1e, 3.4) | 2018 | Ya | Dasar whey/wastewater & anaerobic treatment. |
| [3] Sjafruddin et al. | [3] | Ya (Intro) | 2022 | Ya | Tetap. |
| [4] Basuki et al. | [4] | Ya (Intro) | 2024 | Ya | Tetap. |
| [5] Chitaka & Goga | [5] | Ya (Intro, Methods, 3.1b/d) | 2023 | Ya | Kerangka LCA/karakterisasi. |
| [6] Rosyidah et al. | [6] | Ya (Intro, 3.1a/c) | 2020 | Ya | Dominasi boiling/firewood pada GWP. |
| [7] Nugroho et al. | [7] | Ya (Intro, **3.1a**) | 2024 | Ya | Disitir tambahan di 3.1a untuk menguatkan temuan firewood-boiling. |
| [8] Sari et al. (IOP EES) | [8] | Ya (Intro, Methods) | 2021 | Ya | Dasar functional unit. |
| [9] Hartini et al. | [9] | Ya (Intro, 3.1c) | 2024 | Ya | Ranking freshwater ecotoxicity. |
| [10] Kartika Wardana et al. | [10] | Ya (Intro, Methods) | 2024 | Ya | Tetap. |
| [11] Mir et al. | [11] | Ya (Intro, Methods, 3.2) | 2025 | Ya | Metode AWARE/water scarcity. |
| [12] Saavedra-Rubio et al. | [12] | Ya (Methods 2.2) | 2022 | Ya | Panduan LCI. |
| [13] Satar & Permadi | [13] | Ya (3.4, Tabel 5) | 2022 | Ya | Water recycling/treatment. |
| [14] Ningsih et al. | [14] | Ya (3.4, Tabel 5) | 2026 | Ya | Energy audit/fuel substitution. |

---

## 7. Daftar Bagian yang Diubah & Alasannya

**Introduction**
1. Paragraf 1: ditambah 1 kalimat tentang intensitas energi/firewood agar alur intro → hasil → kesimpulan koheren (GWP kini kategori normalisasi tertinggi). Tanpa referensi baru, tanpa menggeser nomor.

**Methods (klarifikasi, nilai tidak diubah)**
2. 2.1: ditambah pernyataan **tanpa alokasi** (produk tunggal = tofu) dan whey/wastewater sebagai *emission to water*. Alasan: klarifikasi penulis; mencegah hasil per-kg disalahartikan.
3. 2.2: ditegaskan wastewater & whey dimodelkan sebagai *emission to water* (organik + N/P); okara/abu = limbah padat. Disertai **catatan koreksi pelabelan Tabel 1** (pindah baris Wastewater & Whey ke kelompok "Emission to water"; nilai tetap).
4. 2.3: ditambah perlakuan **CO₂ biogenik** dari firewood (carbon-neutral) → menjelaskan GWP boiling. Disertai flag [CHECK DATA] konfirmasi setelan SimaPro.

**Abstract**
5. Hotspot diubah washing→boiling/coagulation; total & ranking diselaraskan; FAET distribusi (34.7/29.5/24.2%); normalisasi GWP tertinggi; AWARE 569 m³ (boiling 51.7%); EP dikaitkan whey *emission to water*.

**Results and Discussion**
6. 3.1a GWP: kontributor boiling 88.0% (bukan washing 67.4%); mekanisme diubah ke CH₄/N₂O + hulu firewood (CO₂ biogenik dikecualikan); +sitasi [7].
7. 3.1b ODP: coagulation 53.8% / boiling 27.2% / molding 13.9%; ditegaskan bukan prioritas.
8. 3.1c FAET: distribusi boiling/coagulation/grinding; grinding=listrik 17 kWh; coagulation=whey *emission to water*.
9. 3.1d AP: coagulation 48.4% / boiling 36.4%; coagulation dikaitkan rantai pasok koagulan (bukan whey, karena AP berbasis emisi udara) — hati-hati agar tidak kontradiksi metode.
10. 3.1e EP: boiling 48.1% / coagulation 38.9%; coagulation = whey kaya N–P (*emission to water*).
11. 3.2 Water Use: total 569; boiling 51.7%, grinding 17.8%, washing 11.5%, soaking 11.1%.
12. 3.3 Normalization: ditulis ulang — GWP tertinggi, FAET kedua, EP ketiga (klaim lama "FAET dominan" dihapus).
13. 3.4 Hotspot: didefinisikan ulang (firewood-boiling; whey coagulation); grinding sebagai driver sekunder FAET. Tabel 5 tetap (masih relevan).

**Conclusion**
14. Total impact, hotspot, ranking normalisasi, dan AWARE 569 diselaraskan; pesan utama digeser ke "climate burden firewood + freshwater impacts organik (whey)".

### Flag manual yang masih perlu Anda cek
- **[Tabel 1]** Reklasifikasi baris **Wastewater** & **Whey** → kelompok *Emission to water* (nilai tetap).
- **[CHECK DATA — biogenic CO₂]** Konfirmasi setelan biogenic carbon SimaPro 10.3 (mendukung narasi GWP).
- **[Figure 2 a–e]** Pastikan grafik kontributor sudah memakai pola baru (boiling/coagulation/grinding dominan; washing minor), bukan grafik lama.
- **[Tabel 3]** Kolom "Share (%)" per stage masih kosong — disarankan diisi: Boiling 51.7, Grinding 17.8, Washing 11.5, Soaking 11.1, Coagulation 6.7, Molding & Packing 1.3.


---

## 8. Addendum — Perbaikan Tabel yang Sudah Diterapkan di ver3 (revisi lanjutan)

Dua dari empat flag manual kini **sudah diterapkan langsung** ke `Alifa Paper Tofu Production ver3.docx` (nilai numerik tidak diubah):

1. **Tabel 1 — reklasifikasi (DONE).** Baris **Wastewater** (2660 / 600 / 100 L) dan **Whey** (10.434 L) dipindahkan dari grup "Output product/material" ke grup kategori baru **"Emission to water"** di akhir tabel. Grup Output kini berisi Tofu Product, Okara, Steam loss, Wood ashes; grup Emission (udara) tetap CO₂/CH₄/N₂O. Semua nilai data tidak berubah.
2. **Tabel 3 — kolom Share (%) diisi (DONE):** Boiling 51.7 · Grinding 17.8 · Soaking 11.1 · Coagulation 6.7 · Washing 11.5 · Molding and Packing 1.3 · Total 100.

Sisa flag yang **masih perlu Anda cek manual** (tidak bisa dipastikan dari sisi teks):
- **[Figure 2 a–e]** Pastikan grafik kontributor memakai pola baru (boiling/coagulation/grinding dominan), bukan grafik washing-dominan lama.
- **[CHECK DATA — biogenic CO₂]** Konfirmasi setelan *biogenic carbon* di SimaPro 10.3 sesuai pernyataan Methods 2.3.

File telah diverifikasi: integritas dokumen (zip) OK, gambar terjaga, kelima tabel terbaca, dan struktur vertical-merge Tabel 1 valid.
