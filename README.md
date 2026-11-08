# Seção 2D interativa — Taió

**Versão 1.0** · Projeto *Taió Plumbing System* (Mestrado em Geologia, UFSC)

🔗 **Acesso:** <https://thubaraleii.github.io/taio-plumbing-system-2d/secao_interativa.html>

Visualizador (Plotly, página única) de seções geológicas transversais sincronizadas com um mapa em planta, para a área do sistema
intrusivo de Taió. A seção é calculada ao longo de qualquer linha de corte sobre o relevo real.

## Funcionalidades

**Barra superior**
- **Linha de corte:** quatro direções livres (horizontal, diagonais e vertical) com **controle deslizante** de deslocamento (passos de 500 m) e clique no mapa para mover o corte; **traçados A–D** fixos (digitalizados em shapefile); e **“Todos os traçados”**, que empilha as quatro seções com rótulos A–D também no mapa.
- **Mapa:** satélite, hipsometria ou geologia atualizada.
- **Exagero vertical:** automático (preenche a área) ou 1×–10×.
- **Camadas:** OSM (rios, estradas e localidades projetados na seção), Campo, Estrutura e Geoquímica.
- **Vista 3D:** diagrama de cortina (fence diagram) com as seções A–D sobre o relevo, com as mesmas unidades e cores.
- **Tema** escuro/claro.

**Seção**
- Topografia real do MDE de drone; unidades sedimentares (Teresina, Serra Alta, Irati, Palermo, Rio Bonito), depósito quaternário, **soleira** e **dique** (amostrados com refinamento nas bordas para que corpos estreitos apareçam).
- **Estruturas:** falhas de campo (preto, com símbolo de falha), falhas CPRM (azul) e fraturas CPRM (rosa tracejado), calculadas no cruzamento da linha de corte com as feições.
- **Pins** de rios, estradas, localidades, pontos de campo e geoquímica, escalonados para evitar sobreposição.
- Zoom e pan nativos do Plotly (duplo clique restaura).

## Dados e métodos

- **Estratigrafia:** contatos como plano de mergulho regional ajustado a pontos de contato Teresina/Serra Alta, com espessuras fixas por unidade (0 / 350 / 430 / 485 / 585 / 854 m de profundidade cumulativa) e erosão pelo relevo real.
- **Quaternário:** onde o terreno está abaixo de 450 m, com 30 m de espessura.
- **Soleira:** do terreno até o topo da Serra Alta (espessura mínima de 27 m); **dique:** coluna vertical até a base do modelo.
- Corpos e unidades são definidos pelos polígonos da litologia atualizada; amostragem de 300 pontos por seção.

## Uso

Abra `secao_interativa.html` no navegador ou acesse a versão publicada. Use a barra superior para escolher a linha de corte; arraste o controle deslizante ou clique no mapa para deslocá-la.

## Regenerar os produtos

O repositório contém o HTML publicado e o script gerador. Para regenerar é necessário o conjunto de dados do projeto
(modelo digital de elevação, litologia, pontos de campo, lineamentos, poços), que **não é distribuído** neste repositório.

```bash
python gerar_secao_interativa.py
```

Dependências Python: `numpy`, `pandas`, `geopandas`, `shapely`, `pyproj`, `rasterio`, `scipy`, `plotly`.

## Estrutura

```
secao_interativa.html        produto gerado
gerar_secao_interativa.py    gerador
assets/                      logotipo e ícones
```

## Referências

1. Milani, E. J.; Melo, J. H. G.; Souza, P. A.; Fernandes, L. A.; França, A. B. (2007). Bacia do Paraná. *Boletim de Geociências da Petrobras*, 15(2), 265–287.
2. Schneider, R. L.; Mühlmann, H.; Tommasi, E.; Medeiros, R. A.; Daemon, R. F.; Nogueira, A. A. (1974). Revisão estratigráfica da Bacia do Paraná. In: *Anais do 28º Congresso Brasileiro de Geologia*, Porto Alegre, SBG, 1, 41–65.
3. Frank, H. T.; Gomes, M. E. B.; Formoso, M. L. L. (2009). Review of the areal extent and the volume of the Serra Geral Formation, Paraná Basin, South America. *Pesquisas em Geociências*, 36(1), 49–57.
4. Peate, D. W. (1997). The Paraná–Etendeka Province. In: Mahoney, J. J.; Coffin, M. F. (eds.), *Large Igneous Provinces*. AGU Geophysical Monograph 100, 217–245.
5. Agafonkin, V. **Leaflet** — an open-source JavaScript library for interactive maps. <https://leafletjs.com>
6. Plotly Technologies Inc. (2015). **Collaborative data science** (Plotly.js). Montréal. <https://plot.ly>
7. Mapzen / Amazon Web Services. **Terrain Tiles** (formato Terrarium). <https://registry.opendata.aws/terrain-tiles/>
8. OpenStreetMap contributors. **OpenStreetMap**. <https://www.openstreetmap.org/copyright>
9. CPRM/SGB — Serviço Geológico do Brasil. **Geologia e Recursos Minerais do Estado de Santa Catarina — Mapa Geológico 1:500.000 (SIG SC)**. <https://geosgb.sgb.gov.br>
10. ANP — Agência Nacional do Petróleo, Gás Natural e Biocombustíveis. **Dados abertos — poços**. <https://www.gov.br/anp>
11. Harris, C. R. et al. (2020). Array programming with NumPy. *Nature*, 585, 357–362.
12. Virtanen, P. et al. (2020). SciPy 1.0: fundamental algorithms for scientific computing in Python. *Nature Methods*, 17, 261–272.
13. Jordahl, K. et al. **GeoPandas**. Zenodo. <https://geopandas.org>; Gillies, S. et al. **Shapely** e **Rasterio**. <https://github.com/shapely/shapely>, <https://github.com/rasterio/rasterio>.

## Licença e uso

- **Código** (scripts de geração e JavaScript das páginas): licença **MIT** — ver [`LICENSE`](LICENSE).
- **Produtos gerados** (HTML, figuras, tabelas derivadas): **CC BY 4.0** — uso, adaptação e redistribuição permitidos com atribuição ao autor.
- **Dados de terceiros** incorporados mantêm as licenças e os termos das fontes originais (tabela em *Créditos e fontes de dados*).
- Os modelos são **interpretativos** e dependem da qualidade e da densidade dos dados de entrada; **não substituem** estudo geológico, hidrogeológico ou geotécnico de detalhe, nem devem ser usados como base única para decisões de engenharia, perfuração ou licenciamento.
- Fornecido “como está”, sem garantias de qualquer tipo.

## Créditos e fontes de dados

| Fonte | Uso | Termos |
|---|---|---|
| Levantamento de campo do autor (pontos, estruturas, geoquímica, MDE de drone) | Dados primários da área de Taió | CC BY 4.0 (autor) |
| CPRM/SGB — Mapa Geológico do Estado de Santa Catarina 1:500.000 (SIG SC) | Geologia regional, falhas, fraturas e diques regionais | Dados abertos CPRM/SGB — citar a fonte |
| ANP — Tabela de poços (dados abertos) | Poços de petróleo/gás (posição e profundidade total) | Dados abertos ANP — citar a fonte |
| Cadastro de poços do Sistema Aquífero Guarani (SAG) | Poços do SAG (posição e profundidade), arquivo KML do projeto | Citar a fonte original do cadastro |
| OpenStreetMap contributors | Rios, estradas e localidades | ODbL 1.0 — © OpenStreetMap contributors |
| Esri World Imagery | Imagem de satélite (tiles e textura) | Termos da Esri — uso com atribuição |
| CARTO / OpenTopoMap | Mapas base do webmap | Atribuição nos próprios mapas (OSM, SRTM, OpenTopoMap CC-BY-SA) |
| AWS Terrain Tiles (formato Terrarium) | Relevo e batimetria regionais (derivados de SRTM, GEBCO e outras fontes) | Atribuição conforme o provedor dos tiles |
| Plotly.js (MIT), Leaflet (BSD-2-Clause) | Bibliotecas de visualização embutidas/carregadas nas páginas | Licenças originais |

## Como citar

> JESUS, A. H. de. **Seção 2D interativa — Taió**, versão 1.0. 2026. Projeto *Taió Plumbing System* — Mestrado em Geologia, UFSC. Disponível em: <https://thubaraleii.github.io/taio-plumbing-system-2d/secao_interativa.html>.

## Autoria

**Afonso Henrique de Jesus** — Mestrado em Geologia, Universidade Federal de Santa Catarina (UFSC).
Projeto: *Architecture and Geochemical Evolution of the Taió Intrusive Plumbing System* (Taió, SC — Bacia do Paraná).
