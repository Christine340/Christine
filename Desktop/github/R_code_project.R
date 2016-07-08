## acf
par(mfrow=c(2,2)) 
acf(Apple, lag=300, main="ACF of residus for Apple")
ccf(Apple,IBM)
ccf(IBM, Apple)
acf(IBM,lag=200, main="ACF of residus for IBM")

## pacf
par(mfrow=c(1,2))
pacf(Apple,main="PACF of Apple",lag=100)
pacf(IBM,main="PACF of IBM",lag=100)

## residual plot 
plot.ts(fit5$residuals,col="blue",main="Detrended Series", ylab="Apple -Trend")

##
resid1=fit5$residuals
install.packages("tseries")
library(tseries)
model1=arma(resid1,order=c(1,1))
summary(model1)

## acf and pacf of Apple
par(mfrow=c(2,2))
acf(Apple,lag=100,main="ACF of Apple")
pacf(Apple,lag=100,main="PACF of Apple")
acf(resid1, lag=100, main="ACF of detrended Apple")
pacf(resid1,main="PACF of detrended Apple",lag=100)


## fit Apple
install.packages("tseries")
library(tseries)
model1=arma(resid1,order=c(5,0))
summary(model1)
## diagonostic: plot of true versus fittted values
par(mfrow=c(1,2))
plot.ts(Y,col="blue",main="Apple Closing Price",ylab="Apple")
plot.ts(model1$fitted.values,col="red",main="Fitted Apple Closing Price:Model1")
## residual
par(mfrow=c(1,2))
plot.ts(Y,col="blue",main="Apple Closing Price",ylab="Apple")
plot.ts(model1$residuals,col="red",main="Residuals Apple Data: Model1")

## compare ACF and PACF of original observations and residuals
par(mfrow=c(2,2))
acf(Y,main="ACF of Apple",lag=100)
acf(model1$residuals,main="ACF of Residuals:Model1",na.action=na.remove,lag=100)
pacf(Y,main="PACF of Apple",lag=100)
pacf(model1$residuals,main="PACF of Residuals:Model1",na.action=na.remove,lag=100)








## apple
model1
t=time(Apple)
fit1=lm(Apple~t)
summary(fit1)
model2
tsq=t^2/factorial(2)
fit2=lm(Apple~t+tsq)
summary(fit2)
model3
tcub=t^3/factorial(3)
fit3=lm(Apple~tcub)
summary(fit3)
model4
fit4=lm(Apple~t+tsq+tcub)
summary(fit4)
model5
fit5=lm(Apple~t+tcub)
summary(fit5)


