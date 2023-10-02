# 제1회 신약개발 AI 경진대회
Link: [https://dacon.io/competitions/official/236127/overview/description](https://dacon.io/competitions/official/236127/overview/description)

> [배경] \
> 국내 신약 소재 데이터의 공유ㆍ활용을 활성화하고, 창의적이고 혁신적인 AI융합인재를 발굴하기 위해 제1회 신약개발 AI 경진대회 “JUMP AI 2023”를 개최합니다.
>
> [주제] \
> 인간과 쥐의 간 대사 효소에 대한 화합물 대사안정성 예측모델 개발 \
> ※ “화합물데이터 공유 및 활용” 아이디어 공모전 동시 개최 ([링크](https://dacon.io/competitions/official/236127/talkboard/408984?page=1&dtype=recent))
> 
> [설명] \
> 화합물의 대사안정성 학습용 데이터 3,498종을 이용해 예측모델을 개발 \
> 개발한 모델로 경진용 데이터 483종 화합물을 이용하여 대사안정성 예측값을 제출


# 1. Data
## 1.1 train.csv
- 3498개 화합물 정보
- id: 샘플 고유 id
- SMILES: 화합물의 분자 구조
- 화합물의 물성 관련 정보 (LogD의 경우 pH값 7.4에서 계산)
- MLM(Mouse Liver Microsome) 포함
- HLM(Human Liver Microsome) 포함
- HLM 및 MLM은 간 및 마우스의 간 대사효소와 화합물을 30분 동안 반응시킨 후, 대사되지 않고 남아있는 화합물의 양을(%) LC-MS/MS로 측정함으로써 화합물의 간 대사효소에 대한 안정성을 평가한 데이터

## 1.2 test.csv
- 483개 화합물 정보
- id: 샘플 고유 id
- SMILES: 화합물의 분자 구조
- 화합물의 물성 관련 정보 (LogD의 경우 pH값 7.4에서 계산)

## 1.3 sample_submission.csv
- id: 샘플 고유 id
- MLM: test 데이터에 대해서 MLM을 예측한 값
- HLM: test 데이터에 대해서 HLM을 예측한 값


# 2. Metrics
- 평가 산식 : 0.5 * RMSE(MLM) + 0.5 * RMSE(HLM)
- Public score : 전체 테스트 데이터 중 약 35%
- Private score : 전체 테스트 데이터



# 1. GIN(Graph Isomorphism Network)
- Paper: [HOW POWERFUL ARE GRAPH NEURAL NETWORKS?](https://arxiv.org/pdf/1810.00826.pdf)


# 2. MGSSL(Motif-based Graph Self-Supervised Learning)
- Paper: [Motif-based Graph Self-Supervised Learning for Molecular Property Prediction](https://arxiv.org/pdf/2110.00987.pdf)
