# モンテカルロ積分

### 概要

モンテカルロ法を用いた積分計算を近似する手法

### 近似対象

$$
\theta = \int_0^1 g(x) dx
$$

### 近似方法

確率変数 $X$ が $X \sim U[0,1]$ であるとき, $g(X)$ の期待値 $E[g(X)]$ に関して以下が成り立つ.

$$
E_{U[0,1]}[g(X)] = \int_0^1 g(x)f_{U[0,1]}(x) dx = \int_0^1 g(x) \times 1 dx = \int_0^1 g(x) dx
$$

これは $g(X)$ の期待値 $E[g(X)]$ の推定量が $\theta$ の近似値になることを意味する.

そこで, $x_1, ..., x_n$ を $U[0,1]$ からサンプリングし, $g(x_1), ..., g(x_n)$ の標本平均を計算することで $\theta$ の近似値とする.

$$
\theta \approx \frac{1}{n} \sum_{i=1}^n g(x_i)
$$

## 区間が $0 \le x \le 1$ でない場合

### 近似対象

$$
\theta = \int_a^b g(x) dx
$$

### 近似方法

$X \sim U[a,b]$ であるとき,

$$
E_{U[a, b]}[g(X)] = \int_a^b g(x) f_{U[a,b]}(x) dx = \frac{1}{b - a} \int_a^b g(x) dx
$$

が成り立つ. そこで, $x_1, ..., x_n$ を $U[a, b]$からサンプリングし,

$$
\theta \approx \frac{b - a}{n} \sum_{i=1}^n g(x_i)
$$

として近似値を得る.

## さらに一般化して

### 近似対象

$$
\theta = E_f[g(x)] = \int_A g(x)f(x) dx
$$

ただし, 関数 $f(x)$ を $A \subset \boldsymbol R$ をサポートにもつ確率密度関数とする.

### 近似方法

確率密度関数 $f(x)$ から無作為標本 $X_1, ..., X_n$ をとり, 標本平均

$$
\hat{\theta} = \bar{g} = \frac{1}{m} \sum_{i=1}^m g(X_i) \tag 🌟
$$

を求めればよい.

## モンテカルロ積分の精度

### モチベーション

$\hat{\theta}$ (🌟) の分散や標準誤差が分かれば, モンテカルロ法で得られる $\hat{\theta}$ の精度が求められる. \
たとえば, 中心極限定理より

$$
\frac{\hat{\theta} - \theta}{\textrm{se}(\hat{\theta})} \leadsto \mathcal{N}(0, 1)
$$

となることを利用すると, $\theta$ に関する信頼区間を構成することもできる. \
そこで, $\hat{\theta}$ の分散と標準誤差を押さえておこう.

> 💡 標準誤差（Standard Error）: 推定量の標準偏差を特に標準誤差という

### $\hat{\theta}$ の分散・標準誤差とその推定量

$g(X)$ の分散を $\sigma^2$ とする.

$$
\begin{align*}
\sigma^2 &\approx \hat{\sigma}^2 := \frac{1}{n} \sum_{i=1}^n (g(X_i) - \hat{\theta})^2 \\
V[\hat{\theta}] &= \frac{\sigma^2}{n} \approx \frac{\hat{\sigma}^2}{n} \\
\textrm{se}(\hat{\theta}) &= \frac{\sigma}{\sqrt{n}} \approx \frac{\hat{\sigma}}{\sqrt{n}}
\end{align*}
$$

## 精度向上

🚨 工事中
