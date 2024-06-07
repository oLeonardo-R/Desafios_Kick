document.getElementById("cep").addEventListener("blur", function () {
  const cep = this.value.replace(/\D/g, "");
  if (cep) {
    fetch(`https://viacep.com.br/ws/${cep}/json/`)
      .then((response) => response.json())
      .then((data) => {
        if (!data.erro) {
          document.getElementById("rua").value = data.logradouro;
          document.getElementById("bairro").value = data.bairro;
          document.getElementById("cidade").value = data.localidade;
          document.getElementById("estado").value = data.uf;
        } else {
          alert("CEP não encontrado.");
        }
      })
      .catch((error) => console.error("Erro ao buscar o CEP:", error));
  }
});
