---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
title: Sobre
---

<div class="about-lang" data-lang="pt" markdown="1">

[Read in English](#){: .lang-switch data-to="en" }

Oi, eu sou o **Lukita**.

Sou Principal Mobile Engineer no **Grupo SBF** e lidero o chapter mobile: cerca de 20 engenheiros e a arquitetura que roda por baixo dos apps do grupo. Os principais:

- **Centauro**, a maior rede multicanal de artigos esportivos da América Latina ([Google Play](https://play.google.com/store/apps/details?id=br.com.sbf.centauro), [App Store](https://apps.apple.com/br/app/id1005641646));
- **Nike Brasil**, da FISIA, a operação oficial da Nike no país ([Google Play](https://play.google.com/store/apps/details?id=br.com.gruposbf.nike), [App Store](https://apps.apple.com/br/app/id6447586622));
- **Spoint**, que transforma treino em pontos ([Google Play](https://play.google.com/store/apps/details?id=br.com.centauro.crava), [App Store](https://apps.apple.com/br/app/spoint/id1596796200)).

Meu dia a dia é **Flutter/Dart** e **Android nativo em Kotlin**. Antes disso já trabalhei com Java, PHP, TypeScript, JavaScript, React, Vue, Node.js e React Native, então quando discuto arquitetura costumo olhar o sistema inteiro, não só o app. No SBF criei o [DoSo](https://github.com/grupo-sbf/DoSo) com o time; antes, na Youse, liderei a [migração do app de nativo para Flutter](/posts/por-que-migrar-de-nativo-para-flutter/).

Também toco a [**remotehub.**](https://remotehub.com.br), minha consultoria, onde sou fundador e tech lead. A receita: apps Flutter com **Clean Architecture** e **BLoC/Cubit**, testes automatizados, cuidado com segurança, e integração com CMS, Firebase, analytics, error tracking e ferramentas de IA, para o cliente conseguir operar e observar o app em produção sem depender de mim.

Gosto de arquitetura limpa, design de software e de coisas que aumentam a produtividade do time. E prefiro decidir junto com produto, design e negócio do que receber a decisão pronta.

Nas horas vagas, sou um engenheiro mobile entediado usando IA para aprender coisas fora da minha área. O experimento mais recente saiu do controle e virou a família **Dinah**: encoders de 150M de parâmetros que tomam decisões tipadas, em português e inglês, rodando no CPU. Treino, avaliação e os erros no caminho ficam todos registrados aqui.

Todo post sai em português e em inglês.

</div>

<div class="about-lang" data-lang="en" markdown="1" hidden>

[Leia em português](#){: .lang-switch data-to="pt" }

Hi, I'm **Lukita**.

I'm a Principal Mobile Engineer at **Grupo SBF**, where I lead the mobile chapter: around 20 engineers and the architecture running underneath the group's apps. The main ones:

- **Centauro**, the largest omnichannel sporting goods retailer in Latin America ([Google Play](https://play.google.com/store/apps/details?id=br.com.sbf.centauro), [App Store](https://apps.apple.com/br/app/id1005641646));
- **Nike Brasil**, by FISIA, Nike's official operation in Brazil ([Google Play](https://play.google.com/store/apps/details?id=br.com.gruposbf.nike), [App Store](https://apps.apple.com/br/app/id6447586622));
- **Spoint**, which turns workouts into points ([Google Play](https://play.google.com/store/apps/details?id=br.com.centauro.crava), [App Store](https://apps.apple.com/br/app/spoint/id1596796200)).

My day to day is **Flutter/Dart** and **native Android with Kotlin**. Before that I worked with Java, PHP, TypeScript, JavaScript, React, Vue, Node.js and React Native, so when I talk architecture I tend to look at the whole system, not just the app. At SBF I built [DoSo](https://github.com/grupo-sbf/DoSo) with the team; before that, at Youse, I led the [app migration from native to Flutter](/posts/why-we-migrated-from-native-to-flutter/).

I also run [**remotehub.**](https://remotehub.com.br), my consultancy, as founder and tech lead. The recipe: Flutter apps with **Clean Architecture** and **BLoC/Cubit**, automated tests, security in mind, and integrations with CMS, Firebase, analytics, error tracking and AI tools, so clients can run and observe their app in production without depending on me.

I like clean architecture, software design and anything that makes a team more productive. And I'd rather make decisions together with product, design and business than get them handed down.

In my spare time, I'm a bored mobile engineer using AI to learn things outside my field. The latest experiment got out of hand and became the **Dinah** family: 150M-parameter encoders that make typed decisions, in Portuguese and English, running on CPU. Training, evaluation and the mistakes along the way are all written down here.

Every post comes out in Portuguese and English.

</div>

<script>
  (function () {
    var blocks = document.querySelectorAll('.about-lang[data-lang]');
    function show(lang, save) {
      blocks.forEach(function (b) { b.hidden = b.dataset.lang !== lang; });
      if (save) { try { localStorage.setItem('lukita-lang', lang); } catch (e) {} }
    }
    document.querySelectorAll('.lang-switch').forEach(function (a) {
      a.addEventListener('click', function (e) { e.preventDefault(); show(a.dataset.to, true); });
    });
    /* same choice as the home filter; with no choice (or "all"), follow the browser language */
    var saved = null;
    try { saved = localStorage.getItem('lukita-lang'); } catch (e) {}
    var browser = ((navigator.languages && navigator.languages[0]) || navigator.language || '').toLowerCase();
    show(saved === 'pt' || saved === 'en' ? saved : (browser.indexOf('pt') === 0 ? 'pt' : 'en'), false);
  })();
</script>
