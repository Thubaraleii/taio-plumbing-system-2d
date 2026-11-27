"""Idioma (PT/EN) e botao de volta ao hub para as paginas do projeto Taio Plumbing System.

Uso (no fim de cada gerador, depois de salvar o HTML):
    import tps_i18n
    tps_i18n.injetar(OUT_HTML, hub=tps_i18n.HUB_TPS)

O bloco injetado e autonomo (CSS + JS): adiciona, ao lado do logotipo, o botao de idioma (PT <-> EN) e o botao "Hub";
traduz a interface em tempo real (nos de texto, atributos, legendas e hover do Plotly, popups do Leaflet e textos 3D)
com um dicionario PT -> EN. A escolha fica em localStorage e viaja entre paginas pelo parametro ?lang=en.
Idempotente: regravar substitui o bloco anterior.
"""
import json
import re
from pathlib import Path

try:
    from tps_i18n_dict import DICT, FRAG, RX
except ImportError:  # pragma: no cover
    DICT, FRAG, RX = {}, [], []

try:
    from tps_info import dados_info
except ImportError:  # pragma: no cover
    dados_info = None

HUB_TPS = "https://tplumbingsystem.github.io/TPS_HUB/"
HUB_ORIGINAL = "https://thubaraleii.github.io/TAIO-HUB/"
INI, FIM = "<!--tps-i18n-->", "<!--/tps-i18n-->"

JS = r"""
(function () {
  if (window.__tpsI18n) return; window.__tpsI18n = true;
  var CFG = __CFG__, DICT = __DICT__, FRAG = __FRAG__, RXS = __RX__.map(function (r) { return [new RegExp(r[0], r[1]), r[2]]; });
  var qs = new URLSearchParams(location.search), stored = null;
  try { stored = localStorage.getItem('tps_lang'); } catch (e) {}
  var lang = qs.get('lang') || stored || 'pt'; if (lang !== 'en') lang = 'pt';
  var cache = {}, MISS = {};
  window.__i18nMiss = MISS;
  var PT_HINT = /[À-ÖØ-öø-ÿ]|\b(de|do|da|dos|das|para|com|sem|por|em|no|na|ao|ou|seção|mapa|camada)\b/i;
  function tr(s) {
    if (!s) return s;
    if (cache[s] !== undefined) return cache[s];
    var m = s.match(/^(\s*)([\s\S]*?)(\s*)$/), core = m[2], out = core;
    if (core && /[A-Za-zÀ-ÿ]/.test(core)) {
      if (Object.prototype.hasOwnProperty.call(DICT, core)) out = DICT[core];
      else {
        for (var i = 0; i < RXS.length; i++) out = out.replace(RXS[i][0], RXS[i][1]);
        for (var j = 0; j < FRAG.length; j++) if (out.indexOf(FRAG[j][0]) >= 0) out = out.split(FRAG[j][0]).join(FRAG[j][1]);
      }
      if (out === core && PT_HINT.test(core) && core.length > 1) MISS[core] = 1;
    }
    var r = m[1] + out + m[3]; cache[s] = r; return r;
  }
  window.__tpsTr = tr;
  var SKIP = {SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, TEXTAREA: 1};
  var ORIG = new WeakMap(), ATTR = new WeakMap(), ATTRS = ['title', 'placeholder', 'aria-label', 'alt'];
  function skip(n) { var p = n.parentNode; return !p || SKIP[p.nodeName] || (p.closest && p.closest('.noi18n')); }
  function procText(n) {
    var rec = ORIG.get(n);
    if (rec && n.data === rec.t) return;
    if (skip(n)) return;
    var o = n.data, t = tr(o); ORIG.set(n, {o: o, t: t}); if (t !== o) n.data = t;
  }
  function procAttr(el, a) {
    var v = el.getAttribute(a); if (v == null) return;
    if (el.closest && el.closest('.noi18n')) return;
    var rec = ATTR.get(el) || {}, r = rec[a];
    if (r && v === r.t) return;
    var t = tr(v); rec[a] = {o: v, t: t}; ATTR.set(el, rec); if (t !== v) el.setAttribute(a, t);
  }
  function walk(root) {
    if (root.nodeType === 3) { procText(root); return; }
    if (root.nodeType !== 1 && root.nodeType !== 11) return;
    if (root.nodeType === 1) { if (SKIP[root.nodeName]) return; ATTRS.forEach(function (a) { if (root.hasAttribute(a)) procAttr(root, a); }); }
    var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT), n;
    while ((n = tw.nextNode())) {
      if (n.nodeType === 3) procText(n);
      else if (!SKIP[n.nodeName]) ATTRS.forEach(function (a) { if (n.hasAttribute(a)) procAttr(n, a); });
    }
  }
  function restaurar() {
    var tw = document.createTreeWalker(document.documentElement, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT), n;
    while ((n = tw.nextNode())) {
      if (n.nodeType === 3) { var rec = ORIG.get(n); if (rec && n.data === rec.t) n.data = rec.o; ORIG.delete(n); }
      else { var ra = ATTR.get(n); if (ra) { Object.keys(ra).forEach(function (a) { if (n.getAttribute(a) === ra[a].t) n.setAttribute(a, ra[a].o); }); ATTR.delete(n); } }
    }
  }
  var T0 = document.title;
  function titulo() { document.title = lang === 'en' ? tr(T0) : T0; }
  // textos 3D (WebGL) vem dos dados do Plotly: traduz/restaura os arrays "text" das series com mode=text
  function plotlyTexto() {
    if (!window.Plotly) return;
    document.querySelectorAll('.js-plotly-plot').forEach(function (gd) {
      if (!gd.data) return;
      gd.__tpsT0 = gd.__tpsT0 || {};
      gd.data.forEach(function (t, i) {
        if (!(t.mode && String(t.mode).indexOf('text') >= 0 && t.text && typeof t.text !== 'string')) return;
        var o = gd.__tpsT0[i] || (gd.__tpsT0[i] = Array.prototype.slice.call(t.text));
        var alvo = lang === 'en' ? o.map(function (s) { return s == null ? s : tr(String(s)); }) : o;
        try { Plotly.restyle(gd, {text: [alvo]}, [i]); } catch (e) {}
      });
    });
  }
  function envolverPlotly() {
    if (!window.Plotly || window.Plotly.__tpsW) return;
    ['newPlot', 'react'].forEach(function (f) {
      var o = Plotly[f]; if (!o) return;
      Plotly[f] = function () { var p = o.apply(this, arguments); if (lang === 'en' && p && p.then) p.then(function () { setTimeout(plotlyTexto, 0); }); return p; };
    });
    Plotly.__tpsW = true;
  }
  // links entre produtos carregam o idioma
  function links() {
    document.querySelectorAll('a[href]').forEach(function (a) {
      var h = a.getAttribute('href'); if (!/^https?:\/\/[^/]*github\.io/i.test(h)) return;
      try { var u = new URL(h); if (lang === 'en') u.searchParams.set('lang', 'en'); else u.searchParams.delete('lang'); a.setAttribute('href', u.toString()); } catch (e) {}
    });
  }
  // botoes (ao lado do logotipo)
  var box = document.createElement('div'); box.id = 'tps-i18n-box'; box.className = 'noi18n';
  box.style.cssText = 'position:fixed;top:' + (CFG.top || 10) + 'px;right:' + (CFG.right || 72) + 'px;z-index:2147483000;display:flex;gap:6px;font:600 12px Inter,Montserrat,Arial,sans-serif';
  var st = document.createElement('style');
  st.textContent = '#tps-i18n-box button{background:rgba(7,23,41,.94);color:#F1F5F9;border:1px solid ' + CFG.acc + ';border-radius:6px;padding:5px 10px;font:inherit;cursor:pointer;line-height:1.2}' +
    '#tps-i18n-box button:hover{background:' + CFG.acc + ';color:#071729}' + (CFG.css || '');
  document.head.appendChild(st);
  var bLang = document.createElement('button'), bHub = null;
  function rotulos() {
    if (bInfo) { bInfo.title = lang === 'en' ? 'References and terms of use' : 'Referências e termos de uso'; bInfo.setAttribute('aria-label', bInfo.title); }
    bLang.textContent = lang === 'en' ? 'PT' : 'EN'; bLang.title = lang === 'en' ? 'Mudar para português' : 'Switch to English';
    if (bHub) { bHub.textContent = '← Hub'; bHub.title = lang === 'en' ? 'Back to the hub' : 'Voltar ao hub'; }
  }
  bLang.onclick = function () { setLang(lang === 'en' ? 'pt' : 'en'); };
  box.appendChild(bLang);
  if (CFG.hub) {
    bHub = document.createElement('button');
    bHub.onclick = function () { var u = new URL(CFG.hub); if (lang === 'en') u.searchParams.set('lang', 'en'); location.href = u.toString(); };
    box.appendChild(bHub);
  }
  // botao de informacoes: referencias, fontes de dados e termos de uso
  var janela = null, aba = 'refs', bInfo = null;
  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; }
  function desenharInfo() {
    if (!janela) return;
    var I = CFG.info, en = lang === 'en', cx = el('div', 'tpsi-caixa');
    cx.setAttribute('role', 'dialog'); cx.setAttribute('aria-modal', 'true');
    var topo = el('div', 'tpsi-topo');
    [['refs', en ? 'References' : 'Referências'], ['termos', en ? 'Terms of use' : 'Termos de uso']].forEach(function (a) {
      var b = el('button', aba === a[0] ? 'tpsi-ativa' : '', a[1]);
      b.onclick = function () { aba = a[0]; desenharInfo(); }; topo.appendChild(b);
    });
    var x = el('button', 'tpsi-fechar', '×'); x.title = en ? 'Close' : 'Fechar'; x.setAttribute('aria-label', x.title); x.onclick = fecharInfo; topo.appendChild(x);
    cx.appendChild(topo);
    var corpo = el('div', 'tpsi-corpo');
    if (aba === 'refs') {
      corpo.appendChild(el('h3', '', en ? 'Data sources' : 'Fontes de dados'));
      var ul = el('ul'); I.fontes[en ? 'en' : 'pt'].forEach(function (f) { ul.appendChild(el('li', '', f)); }); corpo.appendChild(ul);
      corpo.appendChild(el('h3', '', en ? 'References' : 'Referências'));
      var ol = el('ol'); I.refs.forEach(function (r) { ol.appendChild(el('li', '', r)); }); corpo.appendChild(ol);
    } else {
      I.termos[en ? 'en' : 'pt'].forEach(function (t) {
        corpo.appendChild(el('h3', '', t[0]));
        corpo.appendChild(el('p', '', t[1].replace('{titulo}', en ? tr(T0) : T0).replace('{url}', location.origin + location.pathname)));
      });
    }
    cx.appendChild(corpo); janela.textContent = ''; janela.appendChild(cx);
  }
  function teclaInfo(e) { if (e.key === 'Escape') fecharInfo(); }
  function fecharInfo() { if (janela) { janela.remove(); janela = null; document.removeEventListener('keydown', teclaInfo); } }
  function abrirInfo() {
    if (janela) { fecharInfo(); return; }
    janela = el('div', 'noi18n'); janela.id = 'tps-info';
    janela.onclick = function (e) { if (e.target === janela) fecharInfo(); };
    desenharInfo(); document.body.appendChild(janela); document.addEventListener('keydown', teclaInfo);
  }
  if (CFG.info) {
    bInfo = el('button', '', 'ⓘ'); bInfo.onclick = abrirInfo; box.appendChild(bInfo);
    var si = document.createElement('style');
    si.textContent = '#tps-info{position:fixed;inset:0;z-index:2147483600;background:rgba(3,10,19,.72);display:flex;align-items:center;justify-content:center;padding:16px;font:400 13px/1.55 Inter,Montserrat,Arial,sans-serif}' +
      '#tps-info .tpsi-caixa{background:#071729;color:#F1F5F9;border:1px solid ' + CFG.acc + ';border-radius:10px;width:min(720px,100%);max-height:min(80vh,100%);display:flex;flex-direction:column;overflow:hidden;text-align:left}' +
      '#tps-info .tpsi-topo{display:flex;gap:6px;padding:10px 12px;border-bottom:1px solid ' + CFG.acc + '}' +
      '#tps-info button{background:transparent;color:#F1F5F9;border:1px solid ' + CFG.acc + ';border-radius:6px;padding:5px 12px;font:600 12px Inter,Arial,sans-serif;cursor:pointer}' +
      '#tps-info button.tpsi-ativa{background:' + CFG.acc + ';color:#071729}#tps-info .tpsi-fechar{margin-left:auto;font-size:16px;line-height:1}' +
      '#tps-info .tpsi-corpo{overflow:auto;padding:6px 18px 18px}#tps-info h3{font-size:13px;margin:14px 0 6px;color:' + CFG.acc + '}' +
      '#tps-info ul,#tps-info ol{margin:0;padding-left:20px}#tps-info li{margin-bottom:5px}#tps-info p{margin:0;overflow-wrap:anywhere}';
    document.head.appendChild(si);
  }
  function setLang(l) {
    lang = l; try { localStorage.setItem('tps_lang', l); } catch (e) {}
    document.documentElement.lang = l === 'en' ? 'en' : 'pt-br';
    if (l === 'en') walk(document.documentElement); else restaurar();
    titulo(); plotlyTexto(); links(); rotulos(); desenharInfo();
    try { window.dispatchEvent(new Event('tps-lang')); } catch (e) {}
  }
  var mo = new MutationObserver(function (muts) {
    if (lang !== 'en') return;
    muts.forEach(function (m) {
      if (m.type === 'characterData') { if (m.target.nodeType === 3) procText(m.target); }
      else if (m.type === 'attributes') procAttr(m.target, m.attributeName);
      else m.addedNodes.forEach(function (n) { walk(n); });
    });
  });
  function iniciar() {
    var anc = CFG.anchor ? document.querySelector(CFG.anchor) : null;
    if (anc) { box.style.cssText = 'display:flex;gap:6px;align-items:center;margin-right:8px;font:600 12px Inter,Montserrat,Arial,sans-serif'; anc.insertBefore(box, anc.firstChild); }
    else document.body.appendChild(box);
    rotulos(); envolverPlotly();
    mo.observe(document.documentElement, {subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: ATTRS});
    if (lang === 'en') setLang('en'); else { links(); }
  }
  if (document.body) iniciar(); else document.addEventListener('DOMContentLoaded', iniciar);
})();
"""


def _bloco(hub, acc, right, top, css, anchor=None, info=None):
    cfg = dict(hub=hub, acc=acc, right=right, top=top, css=css, anchor=anchor, info=info)
    js = (JS.replace("__CFG__", json.dumps(cfg, ensure_ascii=False))
            .replace("__DICT__", json.dumps(DICT, ensure_ascii=False))
            .replace("__FRAG__", json.dumps(FRAG, ensure_ascii=False))
            .replace("__RX__", json.dumps(RX, ensure_ascii=False)))
    return f"{INI}<script>{js}</script>{FIM}"


def injetar(caminho, hub=HUB_TPS, acc="#13BBE6", right=72, top=10, css="", anchor=None):
    """Injeta (ou substitui) o bloco de idioma/hub antes de </body>. hub=None omite o botao de hub (ex.: no proprio hub)."""
    p = Path(caminho)
    t = p.read_text(encoding="utf-8")
    t = re.sub(re.escape(INI) + r".*?" + re.escape(FIM), "", t, flags=re.S)
    k = t.rfind("</body>")
    bloco = _bloco(hub, acc, right, top, css, anchor, dados_info(p.name) if dados_info else None)
    t = (t[:k] + bloco + t[k:]) if k >= 0 else t + bloco
    p.write_text(t, encoding="utf-8")
    return p
