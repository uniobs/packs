document.addEventListener('DOMContentLoaded', () => {
    const catalogoContainer = document.getElementById('catalogo-container');

    // Função para ler o arquivo CSV
    const lerCSV = async (caminho) => {
        const resposta = await fetch(caminho);
        const dadosTexto = await resposta.text();
        const linhas = dadosTexto.split('\n').map(linha => linha.split(','));

        // Remover a primeira linha se for o cabeçalho
        const cabecalho = linhas.shift();

        // Criar array de objetos com os dados do CSV
        const itens = linhas.map(colunas => {
            const item = {};
            cabecalho.forEach((nomeColuna, index) => {
                item[nomeColuna] = colunas[index];
            });
            return item;
        });

        return itens;
    };

    // Função para exibir o catálogo na página
    const exibirCatalogo = async () => {
        const dados = await lerCSV('dadoscomprada.csv');

        dados.forEach(item => {
            const { nome, preco, conteudo, link } = item;

            // Criar elemento de card para cada item
            const card = document.createElement('div');
            card.classList.add('card');

            // Imagem
            const imagem = document.createElement('img');
            imagem.src = `imagenscomprada/${nome}.png`;
            imagem.alt = nome;
            card.appendChild(imagem);

            // Nome
            const nomeElemento = document.createElement('h2');
            nomeElemento.textContent = nome;
            card.appendChild(nomeElemento);

            // Preço
            const precoElemento = document.createElement('p');
            precoElemento.textContent = `Preço: R$ ${preco}`;
            card.appendChild(precoElemento);

            // Conteúdo
            const conteudoElemento = document.createElement('p');
            conteudoElemento.textContent = conteudo;
            card.appendChild(conteudoElemento);

            // Link
            const linkElemento = document.createElement('a');
            linkElemento.textContent = 'Ver detalhes';
            linkElemento.href = link;
            linkElemento.target = '_blank'; // Abrir o link em uma nova aba
            card.appendChild(linkElemento);

            // Adicionar card ao catálogo
            catalogoContainer.appendChild(card);
        });
    };

    // Chamar função para exibir o catálogo ao carregar a página
    exibirCatalogo();
});
