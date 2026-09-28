---
title: Por que optamos migrar de nativo para o Flutter?
description: Como o time mobile da Youse decidiu trocar o desenvolvimento nativo pelo Flutter, e o que aprendemos no caminho.
date: 2022-03-30 18:27:24 -0300
categories: [Engenharia, Mobile]
tags: [flutter, mobile, youse, arquitetura]
lang: pt-BR
image:
  path: /assets/img/posts/flutter/01.jpeg
  alt: Por que optamos migrar de nativo para o Flutter?
---

[Read in English](/posts/why-we-migrated-from-native-to-flutter/){: .idioma}

> Publicado originalmente no [Youse Tech, no Medium](https://medium.com/youse-tech/por-que-optamos-migrar-de-nativo-para-o-flutter-3dc921612efb), em 30 de março de 2022.
{: .prompt-info }

Não é segredo para nenhum gestor de TI que o desejo de todo desenvolvedor será sempre o de construir soluções robustas, escaláveis e a prova de falhas do ponto de vista de engenharia. Mas ao mesmo tempo, quando olhamos pela perspectiva de produto, essa solução precisa ser inovadora, simples e intuitiva ao usuário. O produto final é o resultado do caminhar entre essa linha tênue que são os pilares descritos anteriormente.

Durante essa jornada de construção de um produto, nos deparamos com certa frequência em determinadas situações que exigem escolhas difíceis, que moldarão nossa solução a longo prazo e que certamente demandarão esforços consideráveis quando tomadas de forma equivocada.

Em 2020, pouco antes do que viria a ser um dos episódios mais tristes e desafiadores para a humanidade desde a segunda guerra mundial, a pandemia do Covid-19, nós do time mobile da Youse nos vimos em um cenário que tem sido comum no mercado de tecnologia atual: a falta de profissionais. Após mais um forte ataque do mercado levar uma parcela relevante dos nossos talentos, estávamos mais uma vez na posição de praticamente apenas um profissional Android e um IOS.

Com um valioso conhecimento e experiências de quase 4 anos de desenvolvimento do nosso aplicativo à mercê de poucas mentes, e uma documentação até então bastante deficitária, foi desperto um primeiro gatilho que culminou na decisão já adiantada no título.

Nosso time, outrora composto por 10 desenvolvedores nativos, sendo cinco deles IOS e os outros cinco Android, conseguiram ao decorrer desse período construir uma aplicação robusta e com funcionalidades incríveis. Mas a Youse não poderia parar por aí, certo?

Por ser a primeira insurtech do Brasil, desde o nascimento, a Youse foi movida pela inovação. Essa determinação e pioneirismo nos deram uma vantagem considerável em relação às grandes seguradoras, até mesmo das mais recentes seguradoras digitais.

Mas, assim como nós, o mercado está a todo vapor e se saindo muito bem! Nossa vantagem inicial se tornava cada vez menor. Era preciso continuar inovando, construindo novas funcionalidades (essas ainda mais incríveis que as anteriores), desenvolver novos produtos que atendessem as necessidades dos nossos clientes e que agregassem valor ao seu dia a dia.

Não é segredo para nenhum desenvolvedor mobile que o desenvolvimento nativo é verboso, com uma trilha de aprendizado longa até se atingir uma proficiência confortável. Desenvolver funcionalidades performáticas e fluídas é um desafio até para os mais experientes! E, ainda com a falta de profissionais experientes e cada vez mais caros na tecnologia nativa, como paralelizar o treinamento e tutoria dos mais juniors com a velocidade da esteira de desenvolvimento que as empresas exigem? Esse foi o nosso segundo gatilho…

Além do desafio que é desenvolver um profissional na tecnologia nativa, ainda há outros pontos que pesam negativamente no contexto da Youse. No final de 2019, o CARGO, nosso design system começava a tomar forma. Com isso, alguns dos desafios que já havíamos enfrentado no passado voltaram à tona, seria preciso, ao menos mais uma vez, refatorar toda nossa UI para se adequar aos novos comportamentos e especificações do cargo; outra vez seria necessário criar especificações levemente (às vezes nem tanto) diferentes entre plataformas para se adequar às guidelines de cada uma…

Nossos times, há algum tempo, já não tinham desenvolvedores em equidades e as funcionalidades eram lançadas com semanas (às vezes até meses) de atrasos entre plataformas. Funcionalidades essas que possuíam diferenças muitas vezes consideráveis em comportamentos e aparência. Esse foi nosso terceiro gatilho…

Antes a galinha de ovos de ouro da Youse era nosso aplicativo, o principal diferencial para qualquer outra seguradora, se tornava um gargalo. Algo precisava ser feito…

**E nós fizemos!**

Uma vez consenso entre todo chapter de que precisávamos mudar, era preciso definir essas mudanças: quais eram as dores do time de produtos e de nós, desenvolvedores? A partir disso, pensamos em algumas premissas que iriam nos guiar na tomada de decisão a fim de solucionar os gatilhos mencionados anteriormente. Essas premissas foram:

- Uma tecnologia multi plataforma que proporcione uma velocidade de desenvolvimento acelerada e uma experiência unificada entre as plataformas;
- Performance mais próxima possível dos nativos
- Barreira de entrada pequena e curva de aprendizado baixa para desenvolvedores de outras stacks;
- Comunidade.
Já em novembro de 2019, iniciamos a busca por tecnologias que cumprissem com as premissas estabelecidas. O nome React Native rapidamente veio à mesa, o time mobile havia recém fundido com o time web para a formação do chapter-frontend, haviam profissionais com proficiência em React e a experiência de alguns do time mobile em projetos passados com a tecnologia, a barreira inicial foi praticamente extinguida e a comunidade React nem precisamos citar, né?

Mas foram justamente essas experiências anteriores de alguns desenvolvedores com o React Native, compartilhada com o time através dos relatos da dificuldade no setup inicial, a forte dependência de bibliotecas de terceiros, além da performance perceptivelmente aquém dos nativos e com a forte rejeição de desenvolvedores nativos devido a barreira que é migrar de código nativo para o javascript que nos fizeram rapidamente desistir dessa possibilidade.

Kotlin Native ainda era um ponto de interrogação na época e não cumpria com o primeiro ponto do cross-platform como desejávamos. Tão logo as tecnologias anteriores eram descartadas, o nome Flutter já se destacava não só entre nós, mas mundialmente. Empresas como a Nubank no Brasil e muitas outras de fora, já divulgavam decisões parecidas como as que buscávamos, tendo Flutter como astro principal.

![Gráfico comparando as buscas por flutter, kotlin e react native no Google. Em set. de 2019 quando iniciamos os estudos internos o flutter tomou a liderança.](/assets/img/posts/flutter/02.png)
_Gráfico comparando as buscas por flutter, kotlin e react native no Google. Em set. de 2019 quando iniciamos os estudos internos o flutter tomou a liderança._

Então rapidamente iniciamos os estudos com o Flutter. Cursos completos foram disponibilizados para o time, dojos, talks e syncs eram realizados semanalmente a fim de discutir o que aprendemos para avançarmos no ecossistema Flutter. O time se adaptou muito rápido e a velocidade de desenvolvimento era impressionante. A diferença de performance era praticamente imperceptível, até aos olhos dos mais atentos, e apesar da comunidade ainda estar em desenvolvimento, estava em pleno crescimento e não foi difícil tomar a decisão de que precisávamos ver, na prática, como o Flutter se comportaria.

Em janeiro, lançamos nossa primeira funcionalidade em flutter, o MGM (Convide Amigos e Ganhe) uma funcionalidade simples, ainda sim, suficiente para que o flutter demonstrasse todo seu poder. A integração com o nosso app nativo foi extremamente fácil, a transição entre Flutter e Nativo era fluída e nem nas mais otimistas das nossas previsões achávamos que o resultado seria tão satisfatório.

![Primeira funcionalidade flutter em produção, a princípio como prova de conceito e experimento. Hoje já refatorada seguindo nossos novos padrões.](/assets/img/posts/flutter/03.gif)
_Primeira funcionalidade flutter em produção, a princípio como prova de conceito e experimento. Hoje já refatorada seguindo nossos novos padrões._

Lembra quando mencionei nos primeiros parágrafos sobre situações que nos desafiam a tomar decisões difíceis e que irão moldar o futuro do nosso produto? Pois é, às vezes elas não são tão difíceis assim…

Após o lançamento da nossa primeira funcionalidade com o Flutter ser um sucesso, iniciamos o incentivo para que os membros do time desenvolvessem suas próximas entregas com ele. Só que rapidamente percebemos que isso não foi uma boa ideia, a coisa não foi tão natural quanto imaginávamos…

Oras, o Flutter não atendeu todas as nossas premissas? Então o que estava dando errado? O time parecia tão engajado nos estudos e animado com o potencial que a tecnologia oferecia… Por que o time não abraçou logo de cara?

A resposta foi tão óbvia e simples que ninguém havia pensado: todos éramos desenvolvedores nativos! Por mais que estivéssemos super empolgados com o Flutter, nossa zona de conforto para entregar uma nova funcionalidade sempre seria o nativo, se tivéssemos opção de escolha! Foi então que, após esse período de um mês, em que poucos decidiram utilizar o Flutter, sentamos, discutimos e decidimos…

**Agora é Flutter e pronto!**

De março em diante, ficou decidido que todas as novas funcionalidades seriam feitas em Flutter em uma migração gradativa sem que nossa esteira de desenvolvimento fosse paralisada, em um processo que dura até hoje, um ano e meio depois. Escrevo esse artigo com a migração próxima ao fim. Tivemos inúmeros desafios desde a criação de uma arquitetura inicial modular multi-package que proporcionasse uma migração gradativa fácil e desacoplada, até em uma arquitetura de gerenciamento de estados padronizada e robusta, na construção de um design system com uma experiência unificada, e em uma cobertura de testes abrangente.

Tudo isso com um time que hoje é metade do que tínhamos a 2 anos atrás, mas com uma velocidade de desenvolvimento senão próxima, ainda mais rápida! O veredito final não poderia ter sido outro. Nossa decisão se mostrou positiva e com uma ótima perspectiva para o futuro: em um ano com o Flutter e em um processo ainda em transição, já colhemos frutos que nos fazem acreditar que essa foi a decisão correta.

Provavelmente, você desenvolvedor que irá iniciar um projeto, ou que trabalha em uma empresa cujo cenário era parecido com o nosso, que tem tido as mesmas dores que relatei, neste momento deve estar se perguntando: devo seguir o mesmo caminho?

A resposta óbvia é: não sei! Sou defensor de que cada caso é um caso, cada projeto é um projeto, mas posso afirmar com certeza que o Flutter é uma solução robusta, madura o suficiente e com uma velocidade de desenvolvimento absurda e a facilidade de aprendizado que qualquer empresa de tecnologia necessita hoje. Se eu puder te dar uma dica, ela seria: considere o Flutter, busque por ele, provavelmente ele irá atender às suas necessidades e te poupará um precioso tempo.

Por fim, antes de mais nada, nesse artigo eu relatei a minha experiência como um desenvolvedor nativo que encabeçou essa mudança interna. Ela só foi possível com a ajuda de um time multidisciplinar e engajado, de uma empresa e liderança compradas com o time e proporcionando autonomia total nas tomadas de decisões.

Se você quer saber mais sobre os desafios que encontramos, decisões de desenvolvimento que tomamos, sinta-se à vontade para comentar e perguntar qualquer coisa!

Caso tenha interesse em participar dessa jornada conosco, temos vagas abertas e um mundo inteiro de desafios e funcionalidades a desbravar pós-migração.

Vagas: [https://jobs.kenoby.com/vagas-youse/job/dev-mobileflutter/6102ba438f605b6168853b77?utm_source=website](https://jobs.kenoby.com/vagas-youse/job/dev-mobileflutter/6102ba438f605b6168853b77?utm_source=website)
