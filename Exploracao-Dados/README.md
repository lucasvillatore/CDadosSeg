### Dataset utilizado

Foi utilizado o dataset relacionado a **ataque de negação de serviço (DDoS)**
Esse dataset é disponibilizado nesse link: https://www.kaggle.com/devendra416/ddos-datasets



- Que tipos de dados você tem, majoritariamente (atributos numéricos, textuais) ?

  Esse dataset possui dados majoritariamente númericos, como por exemplo IP's, portas, número de bytes de sobre algum dado ou dados relacionados a tempo.

- Qual seu objetivo com esse dataset?
  Conseguir descobrir tendências de ataques, como por exemplo horário mais prováveis de ocorrer um ataque DDoS, qual a duranção dele, qual foi o tipo de ataque.

  

- Seu dataset é rotulado de que maneira?
  

  

- Como é a distribuição dos dados do dataset?
  



- Quais colunas/atributos você julga ser interessante manter e remover? Por quê?
  Flow ID,
  Src IP - Source IP,
  Src Port - Source Port,
  Dst IP - Destination IP,
  Timestamp ,
  Tot Fwd Pkts - Total Foward Packages,
  Flow IAT Min - Minimum time between two flows,
  Init Bwd Win Byts - # of bytes sent in initial window in the backward direction,
  Fwd Seg Size Min - Average size observed in the forward direction,
  Label - Label



Abaixo podemos ver os campos presentes, os campos dados como mais importantes estão destacados em negrito. São estes:

- **Flow ID**
- **Src IP**
- **Src Port**
- **Dst IP**
- Dst Port
- Protocol
- **Timestamp**
- Flow Duration
- **Tot Fwd Pkts**
- Tot Bwd Pkts
- TotLen Fwd Pkts
- TotLen Bwd Pkts
- Fwd Pkt Len Max
- Fwd Pkt Len Min
- Fwd Pkt Len Mean
- Fwd Pkt Len Std
- Bwd Pkt Len Max
- Bwd Pkt Len Min
- Bwd Pkt Len Mean
- Bwd Pkt Len Std
- Flow Byts/s
- Flow Pkts/s
- Flow IAT Mean
- Flow IAT Std
- Flow IAT Max
- **Flow IAT Min**
- Fwd IAT Tot
- Fwd IAT Mean
- Fwd IAT Std
- Fwd IAT Max
- Fwd IAT Min
- Bwd IAT Tot
- Bwd IAT Mean
- Bwd IAT Std
- Bwd IAT Max
- Bwd IAT Min
- Fwd PSH Flags
- Bwd PSH Flags
- Fwd URG Flags
- Bwd URG Flags
- Fwd Header Len
- Bwd Header Len
- Fwd Pkts/s
- Bwd Pkts/s
- Pkt Len Min
- Pkt Len Max
- Pkt Len Mean
- Pkt Len Std
- Pkt Len Var
- FIN Flag Cnt
- SYN Flag Cnt
- RST Flag Cnt
- PSH Flag Cnt
- ACK Flag Cnt
- URG Flag Cnt
- CWE Flag Count
- ECE Flag Cnt
- Down/Up Ratio
- Pkt Size Avg
- Fwd Seg Size Avg
- Bwd Seg Size Avg
- Fwd Byts/b Avg
- Fwd Pkts/b Avg
- Fwd Blk Rate Avg
- Bwd Byts/b Avg
- Bwd Pkts/b Avg
- Bwd Blk Rate Avg
- Subflow Fwd Pkts
- Subflow Fwd Byts
- Subflow Bwd Pkts
- Subflow Bwd Byts
- Init Fwd Win Byts
- **Init Bwd Win Byts**
- Fwd Act Data Pkts
- **Fwd Seg Size Min**
- Active Mean
- Active Std
- Active Max
- Active Min
- Idle Mean
- Idle Std
- Idle Max
- Idle Min
- Label