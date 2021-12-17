<h1 align="center">Cepheus 🚀 </h1>

<p align="center">Nesse projeto, foi desenvolvido uma aplicação RESTful para listagem de lançamentos de missões espaciais.</p>

<h1>Pré-requisitos</h1>

Antes de começar, você vai precisar apertar os cintos, porque foquete não tem ré 😉

<br>

<strong>ENDPOINT BASE</strong>
```bash
https://apicepheus.leandroguezinjunior.com
```

<br>

<strong>ENDPOINT 👉 listar o último lançamento</strong>

```bash
curl -X GET "https://apicepheus.leandroguezinjunior.com/v1/latest/launch"
```

**_Response_**

```json
{
  "mission": "IXPE",
  "success": true,
  "details": null,
  "date_utc": "2021-12-09T06:00:00.000Z",
  "rocket": {
    "name": "Falcon 9",
    "cost_per_launch": 50000000,
    "description": "O Falcon 9 é um foguete de dois estágios projetado e fabricado pela SpaceX para o transporte confiável e seguro de satélites e a espaçonave de dragão em órbita."
  }
}
```

<br>

<strong>ENDPOINT 👉 listar os próximos lançamentos</strong>

```bash
curl -X GET "https://apicepheus.leandroguezinjunior.com/v1/upcoming/launches"
```

**_Response_**

```json
[
  {
    "mission": "Starlink 4-4 (v1.5)",
    "date_utc": "2021-12-18T09:24:40.000Z"
  },
  {
    "mission": "Türksat 5B",
    "date_utc": "2021-12-19T03:58:00.000Z"
  },
  {
    ...
  }
]
```

<br>

<strong>ENDPOINT 👉 listar os lançamentos passados</strong>

```bash
curl -X GET "https://apicepheus.leandroguezinjunior.com/v1/past/launches"
```

**_Response_**

```json
[
  {
    "mission": "DemoSat",
    "success": false,
    "details": "Been e transição de primeira etapa bem sucedida para o segundo estágio, máxima altitude 289 km, desligamento de motor prematuro em T + 7 min 30 s, não conseguiu alcançar órbita, não conseguiu recuperar o primeiro estágio",
    "date_utc": "2007-03-21T01:10:00.000Z",
    "rocket": {
      "name": "Falcon 1",
      "cost_per_launch": 6700000,
      "description": "O Falcon 1 foi um sistema de lançamento despendível desenvolvido e fabricado pela SpaceX durante 2006-2009.Em 28 de setembro de 2008, o Falcon 1 tornou-se o primeiro veículo de lançamento de combustível líquido desenvolvido de forma privada para ir em órbita ao redor da Terra."
    }
  },
  {
    "mission": "FalconSat",
    "success": false,
    "details": "Falha do motor a 33 segundos e perda de veículo",
    "date_utc": "2006-03-24T22:30:00.000Z",
    "rocket": {
      "name": "Falcon 1",
      "cost_per_launch": 6700000,
      "description": "O Falcon 1 foi um sistema de lançamento despendível desenvolvido e fabricado pela SpaceX durante 2006-2009.Em 28 de setembro de 2008, o Falcon 1 tornou-se o primeiro veículo de lançamento de combustível líquido desenvolvido de forma privada para ir em órbita ao redor da Terra."
    }
  },
  {
    ...
  }
]
```

<br>

<strong>ENDPOINT 👉 listar o próximo lançamento</strong>

```bash
curl -X GET "https://apicepheus.leandroguezinjunior.com/v1/next/launch"
```

**_Response_**

```json
{
  "mission": "Starlink 4-4 (v1.5)",
  "details": null,
  "date_utc": "2021-12-18T09:24:40.000Z",
  "rocket": {
    "name": "Falcon 9",
    "cost_per_launch": 50000000,
    "description": "O Falcon 9 é um foguete de dois estágios projetado e fabricado pela SpaceX para o transporte confiável e seguro de satélites e a espaçonave de dragão em órbita."
  }
}
```

<br>

<h1>🛠 Tecnologias</h1>

As seguintes ferramentas foram usadas na construção do projeto:

- Linguagem [Python 3.8](https://www.python.org/)
- AWS Serverless Application Model - [SAM](https://aws.amazon.com/serverless/sam/)
- [AWS API Gateway](https://aws.amazon.com/pt/api-gateway/)
- [AWS Lambda](https://aws.amazon.com/pt/lambda/)
- Amazon Route 53 - [DNS](https://aws.amazon.com/pt/route53/)
- Google translate API [Googletrans](https://py-googletrans.readthedocs.io/en/latest/)
- GitHub Actions - [CI/CD](https://github.com/features/actions)


<br>
<br>

Dados consumidos através da [SpaceX-API](https://github.com/r-spacex/SpaceX-API/tree/master/docs#rspacex-api-docs)
