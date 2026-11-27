"""Conteudo do botao de informacoes (referencias, fontes de dados e termos de uso), bilingue, por produto."""

# ------------------------------------------------------------------ referencias
BACIA = [
    "Milani, E. J.; Melo, J. H. G.; Souza, P. A.; Fernandes, L. A.; França, A. B. (2007). Bacia do Paraná. Boletim de Geociências da Petrobras, 15(2), 265–287.",
    "Schneider, R. L.; Mühlmann, H.; Tommasi, E.; Medeiros, R. A.; Daemon, R. F.; Nogueira, A. A. (1974). Revisão estratigráfica da Bacia do Paraná. Anais do 28º Congresso Brasileiro de Geologia, Porto Alegre, SBG, 1, 41–65.",
    "Frank, H. T.; Gomes, M. E. B.; Formoso, M. L. L. (2009). Review of the areal extent and the volume of the Serra Geral Formation, Paraná Basin, South America. Pesquisas em Geociências, 36(1), 49–57.",
    "Peate, D. W. (1997). The Paraná–Etendeka Province. In: Mahoney, J. J.; Coffin, M. F. (eds.), Large Igneous Provinces. AGU Geophysical Monograph 100, 217–245.",
]
GEOQ = [
    "Peate, D. W.; Hawkesworth, C. J.; Mantovani, M. S. M. (1992). Chemical stratigraphy of the Paraná lavas (South America): classification of magma types and their spatial distribution. Bulletin of Volcanology, 55, 119–139.",
    "Bellieni, G. et al. (1984). High- and low-TiO₂ flood basalts from the Paraná plateau (Brazil): petrology and geochemical aspects bearing on their mantle origin. Neues Jahrbuch für Mineralogie, Abhandlungen, 150, 273–306.",
    "Le Bas, M. J.; Le Maitre, R. W.; Streckeisen, A.; Zanettin, B. (1986). A chemical classification of volcanic rocks based on the total alkali–silica diagram. Journal of Petrology, 27, 745–750.",
    "Irvine, T. N.; Baragar, W. R. A. (1971). A guide to the chemical classification of the common volcanic rocks. Canadian Journal of Earth Sciences, 8, 523–548.",
    "Shand, S. J. (1943). Eruptive Rocks. 2nd ed. New York: John Wiley & Sons.",
    "Maniar, P. D.; Piccoli, P. M. (1989). Tectonic discrimination of granitoids. Geological Society of America Bulletin, 101, 635–643.",
    "McDonough, W. F.; Sun, S.-s. (1995). The composition of the Earth. Chemical Geology, 120, 223–253.",
    "Shervais, J. W. (1982). Ti–V plots and the petrogenesis of modern and ophiolitic lavas. Earth and Planetary Science Letters, 59, 101–118.",
    "Harker, A. (1909). The Natural History of Igneous Rocks. London: Methuen.",
]
DIRECAO = [
    "Mardia, K. V.; Jupp, P. E. (2000). Directional Statistics. Chichester: John Wiley & Sons.",
    "Fisher, N. I. (1993). Statistical Analysis of Circular Data. Cambridge: Cambridge University Press.",
]

# ------------------------------------------------------------------ fontes de dados: (pt, en)
F = {
    "campo": ("Levantamento de campo do autor (pontos, estruturas, geoquímica, MDE de drone).",
              "Author's field survey (points, structures, geochemistry, drone DEM)."),
    "cprm": ("CPRM/SGB — Mapa Geológico de Santa Catarina 1:500.000 (SIG SC).",
             "CPRM/SGB — Geological Map of Santa Catarina 1:500,000 (SIG SC)."),
    "anp": ("ANP — dados abertos, tabela de poços.", "ANP — open data, well table."),
    "sag": ("CPRM (2013) — Mapa Hidrogeológico de Santa Catarina, Tabela 7 (poços do Sistema Aquífero Guarani, RH7).",
            "CPRM (2013) — Hydrogeological Map of Santa Catarina, Table 7 (Guarani Aquifer System wells, RH7)."),
    "pmp": ("Compilação de poços ANP/CPRM do projeto PMP: topos de unidade e intervalos intrusivos.",
            "ANP/CPRM well compilation from the PMP project: unit tops and intrusive intervals."),
    "osm": ("© OpenStreetMap contributors (ODbL 1.0).", "© OpenStreetMap contributors (ODbL 1.0)."),
    "esri": ("Esri World Imagery (termos da Esri).", "Esri World Imagery (Esri terms of use)."),
    "mapas": ("Mapas base CARTO e OpenTopoMap (CC-BY-SA), conforme a atribuição nos mapas.",
              "CARTO and OpenTopoMap (CC-BY-SA) base maps, as attributed on the maps."),
    "dem": ("AWS Terrain Tiles (relevo e batimetria; derivados de SRTM, GEBCO e outras fontes).",
            "AWS Terrain Tiles (relief and bathymetry; derived from SRTM, GEBCO and other sources)."),
    "libs": ("Bibliotecas Plotly.js (MIT) e Leaflet (BSD-2-Clause).", "Plotly.js (MIT) and Leaflet (BSD-2-Clause) libraries."),
}

PERFIS = {
    "webmap": (["campo", "cprm", "anp", "sag", "osm", "esri", "mapas", "libs"], BACIA),
    "dashboard": (["campo", "osm", "esri", "mapas", "libs"], GEOQ + BACIA),
    "secao": (["campo", "cprm", "osm", "esri", "libs"], BACIA),
    "modelo3d": (["campo", "cprm", "esri", "libs"], BACIA),
    "zoom": (["campo", "cprm", "anp", "sag", "esri", "libs"], BACIA),
    "furos": (["campo", "cprm", "anp", "sag", "pmp", "dem", "libs"], BACIA),
    "panorama": (["campo", "cprm", "anp", "sag", "pmp", "dem", "esri", "libs"], BACIA + DIRECAO),
    "hub": (["campo", "cprm", "anp", "sag", "pmp", "dem", "osm", "esri", "mapas", "libs"], BACIA + GEOQ + DIRECAO),
}

ARQUIVOS = [("webmap", "webmap"), ("dashboard", "dashboard"), ("secao", "secao"), ("viewer_3d", "modelo3d"),
            ("zooms_3d", "zoom"), ("regional_furos", "furos"), ("panorama", "panorama"), ("index", "hub")]

TERMOS = {
    "pt": [
        ("Autoria", "Afonso Henrique de Jesus — Mestrado em Geologia, UFSC. Projeto Taió Plumbing System."),
        ("Licença", "Código: MIT. Produtos gerados (páginas, figuras e tabelas derivadas): CC BY 4.0, com atribuição ao autor. Dados de terceiros mantêm as licenças e os termos das fontes originais."),
        ("Natureza dos modelos", "Os modelos são interpretativos e dependem da qualidade e da densidade dos dados. Extrapolações e elementos esquemáticos (como o rejeito do horst e as superfícies longe dos poços) não são medidas."),
        ("Limitação de uso", "Não substituem estudo geológico, hidrogeológico ou geotécnico de detalhe e não devem ser a única base para decisões de engenharia, perfuração ou licenciamento."),
        ("Garantia", "Fornecido “como está”, sem garantias de qualquer tipo."),
        ("Como citar", "JESUS, A. H. de. {titulo}, versão 1.0. 2026. Taió Plumbing System, UFSC. Disponível em: {url}."),
    ],
    "en": [
        ("Authorship", "Afonso Henrique de Jesus — MSc in Geology, UFSC. Taió Plumbing System project."),
        ("License", "Code: MIT. Generated products (pages, figures and derived tables): CC BY 4.0, with attribution to the author. Third-party data keep the licenses and terms of their original sources."),
        ("Nature of the models", "The models are interpretive and depend on data quality and density. Extrapolations and schematic elements (such as the horst throw and surfaces far from wells) are not measurements."),
        ("Limitation of use", "They do not replace a detailed geological, hydrogeological or geotechnical study and must not be the sole basis for engineering, drilling or permitting decisions."),
        ("Warranty", "Provided “as is”, without warranties of any kind."),
        ("How to cite", "JESUS, A. H. de. {titulo}, version 1.0. 2026. Taió Plumbing System, UFSC. Available at: {url}."),
    ],
}


def dados_info(nome_arquivo):
    """Estrutura serializavel usada pelo JS do botao de informacoes, escolhida pelo nome do HTML."""
    n = nome_arquivo.lower()
    perfil = next((p for chave, p in ARQUIVOS if chave in n), "hub")
    fontes, refs = PERFIS[perfil]
    return dict(fontes={"pt": [F[k][0] for k in fontes], "en": [F[k][1] for k in fontes]}, refs=refs, termos=TERMOS)
