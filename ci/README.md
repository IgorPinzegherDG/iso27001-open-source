# Integração contínua

O arquivo `validar.yml` deste diretório é o fluxo do GitHub Actions que:

1. regenera a documentação e falha se o resultado divergir de
   `dados/controles.yaml`, impedindo que os arquivos gerados fiquem
   desatualizados;
2. verifica se todas as URLs ainda respondem, a cada alteração e semanalmente,
   porque link morre sem que ninguém toque no repositório.

Ele mora aqui, e não em `.github/workflows/`, apenas porque versionar fluxo de
trabalho exige o escopo `workflow` no token. Para ativá-lo:

```bash
gh auth refresh -s workflow
mkdir -p .github/workflows
git mv ci/validar.yml .github/workflows/validar.yml
git commit -m "Ativa a validação no CI"
git push
```
