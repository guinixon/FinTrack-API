const API = 'http://localhost:8000/financeiro';

let transacoes = [];

async function carregarDados() {
    const res = await fetch(`${API}/transacoes`);
    transacoes = await res.json();
    renderizar();
}

function renderizar() {
    const lista = document.getElementById('listarTransacoes');

    lista.innerHTML = "";

    let entradas = 0;
    let saidas = 0;

    transacoes.forEach(t => {
        const li = document.createElement("li");

        li.classList.add(t.tipo);

        li.innerHTML = `
            <span>${t.descricao}</span>
            <strong>R$ ${t.valor}</strong>
        `;

        lista.appendChild(li);

        if (t.tipo === "entrada")
            entradas += t.valor;
        else
            saidas += t.valor;
    });

    document.getElementById("entradas").innerText = "R$ " + entradas;
    document.getElementById("saidas").innerText = "R$ " + saidas;
    document.getElementById("saldo").innerText = "R$ " + (entradas - saidas);
}

async function criarTransacao() {

    const descricao = document.getElementById("descricao").value;
    const valor = Number(document.getElementById("valor").value);
    const tipo = document.getElementById("tipo").value;
    const categoria = document.getElementById("categoria").value;

    if (!descricao || !valor) {
        alert("Preencha todos os campos");
        return;
    }

    const transacao = {
        id: Date.now(),
        descricao,
        valor,
        tipo,
        categoria
    };

    await fetch(`${API}/transacoes`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(transacao)
    });
    

    carregarDados();
}

carregarDados();