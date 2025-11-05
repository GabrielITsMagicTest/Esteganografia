Perfeito 👍 — aqui está **tudo pronto e formatado corretamente para GitHub**, com um único bloco que você pode **copiar e colar direto no terminal ou editor**.
Inclui **README.md**, **requirements.txt** e **LICENSE (MIT)** — já prontos, limpos e com bom visual no GitHub.

---

```bash
# ========================
# 📄 ARQUIVO: README.md
# ========================
cat > README.md <<'EOF'
# 🕵️‍♂️ Projeto de Esteganografia com Criptografia

> Ferramenta simples de **esteganografia em imagens** (ocultação de texto dentro de PNG/JPG) com suporte a **criptografia** (AES, Blowfish, ChaCha20 e Salsa20).  
> **Feito por ChatGPT (OpenAI)**

---

## 📘 Descrição

Este projeto permite esconder mensagens de texto dentro de imagens, alterando discretamente os bits menos significativos (LSB) dos pixels RGB.  
Antes de embutir o texto, o conteúdo pode ser **criptografado** usando um dos algoritmos disponíveis:

- AES (`AesHelper`)
- Blowfish (`BlowfishHelper`)
- ChaCha20 (`ChaChaHelper`)
- Salsa20 (`SalsaHelper`)

O código principal está em:

```

./Esteganografia/Esteganografia.py

```

---

## 🧩 Estrutura de diretórios

```

.
├── Esteganografia/
│   └── Esteganografia.py
├── ciphers/
│   ├── aes.py
│   ├── blowfish.py
│   ├── chacha20.py
│   └── salsa20.py
├── requirements.txt
└── README.md

```

---

## ⚙️ Requisitos

O arquivo `requirements.txt` deve conter:

```

Pillow>=9.0.0
pycryptodome>=3.16.0
cryptography>=40.0.0

````

### Instalação

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

#### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 🚀 Como usar

### 1. Configure o script

No início do arquivo `Esteganografia.py`, ajuste as variáveis:

```python
path_imagem = "/hacker.png"       # Caminho da imagem base
cipher = ChaChaHelper             # Algoritmo de criptografia
key = "123456"                    # Chave de criptografia
```

O script automaticamente concatena o diretório atual (`DIRNAME`) com o caminho da imagem.

---

### 2. Execute o script

Após instalar as dependências e ajustar o caminho da imagem:

```bash
python3 ./Esteganografia/Esteganografia.py
```

Ele irá:

* Criar uma nova imagem com o texto oculto (exemplo: `hacker_stegano_.png`)
* Ler e decodificar a mensagem embutida
* Exibir o resultado no console

---

## 🧠 Como funciona

Cada caractere da mensagem é convertido em binário (`8 bits`) e gravado nos **bits menos significativos** dos pixels da imagem.

* Cada caractere usa **3 pixels (9 valores RGB)**.
* O último bit de cada grupo indica se a leitura deve parar (fim da mensagem).
* O método `encode()` insere os dados.
* O método `decode()` extrai os dados e, se houver cifragem, faz a decifragem automática.

---

## 💡 Exemplo programático

```python
from Esteganografia.Esteganografia import SteganoHelper
from ciphers.chacha20 import ChaChaHelper

key = "123456".ljust(32, "s").encode()
cipher = ChaChaHelper(key)

stg = SteganoHelper(crypt=cipher)
stg.encode("/full/path/to/image.png", "Mensagem secreta", prefix="stegano")

mensagem = stg.decode("/full/path/to/image_stegano_.png")
print("Mensagem decodificada:", mensagem)
```

---

## ⚠️ Dicas e Cuidados

* **Use chaves fortes.** Evite senhas curtas como `"123456"`.
  Gere uma chave com `os.urandom(32)` ou `get_random_bytes(32)`.
* **Tamanho da imagem:** quanto maior a imagem, mais texto ela pode conter.
* **UTF-8:** para suportar acentos e caracteres especiais, adapte `genData()` para usar `data.encode("utf-8")`.
* **Imagem de saída:** é salva como `<nome>_stegano_.png` por padrão.
* **Evite imagens muito pequenas**, pois a mensagem pode ultrapassar o número de pixels disponíveis.

---

## 🧰 Melhorias sugeridas

* Implementar interface CLI com `argparse` para uso via linha de comando.
* Adicionar suporte a leitura de mensagens de arquivos de texto.
* Mostrar tamanho máximo de mensagem suportada pela imagem.
* Adicionar tratamento de exceções e mensagens de erro mais detalhadas.

---

## 🪶 Exemplo de resultado

```bash
$ python3 Esteganografia/Esteganografia.py
foi obtido da imagem: <texto que sera criptografado> suporta muitas linhas hahahahahhahahahhaaahhaahahahhahah mas tem quer ser grande o arquivo haha
```

---

## 🔒 Segurança

Esteganografia **não substitui criptografia** — apenas oculta dados.
Combine os dois (como neste projeto) para maior segurança.

* Prefira algoritmos modernos (ChaCha20 ou AES-256).
* Evite reutilizar chaves ou imagens públicas.

---

## 🧾 Licença

Licença livre (MIT).
Sinta-se à vontade para modificar, estudar e distribuir.

---

## ✍️ Autor

**Feito por ChatGPT (OpenAI)**

> Este README foi gerado automaticamente com base no código fornecido.
> EOF

# ========================

# 📦 ARQUIVO: requirements.txt

# ========================

cat > requirements.txt <<'EOF'
Pillow>=9.0.0
pycryptodome>=3.16.0
cryptography>=40.0.0
EOF

# ========================

# ⚖️ ARQUIVO: LICENSE (MIT)

# ========================

cat > LICENSE <<'EOF'
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
EOF

````

---

✅ **Como usar:**

1. Copie **todo o bloco acima** (do início até o fim).  
2. Cole no terminal Linux dentro da pasta do seu projeto.  
3. Isso vai criar automaticamente:
   - `README.md` (formatado corretamente)
   - `requirements.txt`
   - `LICENSE`

Depois é só fazer:

```bash
git add README.md requirements.txt LICENSE
git commit -m "Adiciona documentação e licença"
git push
````

---

Quer que eu adicione a esse mesmo script a criação automática do `.gitignore` também (para ignorar `.venv`, `__pycache__`, imagens etc.)?
