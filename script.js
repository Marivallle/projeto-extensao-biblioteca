const catalogo = [];

document.getElementById('adicionar').addEventListener('click', () => {
    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;
    const ano = document.getElementById('ano').value;
    
    if (titulo && autor && ano) {
        const livro = { titulo, autor, ano, disponivel: true };
        catalogo.push(livro);
        atualizarCatalogo();
        limparCampos();
    } else {
        alert('Por favor, preencha todos os campos.');
    }
});

document.getElementById('retirar').addEventListener('click', () => {
    const titulo = document.getElementById('livro').value;
    const livro = catalogo.find(l => l.titulo.toLowerCase() === titulo.toLowerCase());

    if (livro) {
        if (livro.disponivel) {
            livro.disponivel = false;
            atualizarCatalogo();
            alert(`Você retirou o livro: '${livro.titulo}'`);
        } else {
            alert(`O livro '${livro.titulo}' já foi retirado.`);
        }
    } else {
        alert(`Livro '${titulo}' não encontrado.`);
    }
});

document.getElementById('devolver').addEventListener('click', () => {
    const titulo = document.getElementById('livro').value;
    const livro = catalogo.find(l => l.titulo.toLowerCase() === titulo.toLowerCase());

    if (livro) {
        if (!livro.disponivel) {
            livro.disponivel = true;
            atualizarCatalogo();
            alert(`Você devolveu o livro: '${livro.titulo}'`);
        } else {
            alert(`O livro '${livro.titulo}' já está disponível.`);
        }
    } else {
        alert(`Livro '${titulo}' não encontrado.`);
    }
});

function atualizarCatalogo() {
    const catalogoUl = document.getElementById('catalogo');
    catalogoUl.innerHTML = '';
    
    catalogo.forEach(livro => {
        const li = document.createElement('li');
        li.textContent = `${livro.titulo}, por ${livro.autor} (${livro.ano}) - ${livro.disponivel ? 'Disponível' : 'Indisponível'}`;
        catalogoUl.appendChild(li);
    });
}

function limparCampos() {
    document.getElementById('titulo').value = '';
    document.getElementById('autor').value = '';
    document.getElementById('ano').value = '';
}
