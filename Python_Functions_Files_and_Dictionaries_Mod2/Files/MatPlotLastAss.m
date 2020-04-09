clc
close all
clearvars

%retweet_count,reply_count,pos_score,neg_score,net_score
Data = csvread('D:\Github\Coursera_Python_3_Programming_Michigan\Python_Functions_Files_and_Dictionaries_Mod2\Files\resulting_data.csv',1,0);

net_score = Data(:,5);
ret_count = Data(:,1);

figure
scatter(net_score,ret_count,75,'O','filled')
xlabel('Net Score')
ylabel('Number of Retweets')
title('Sentiment Analysis Results')
grid on
set(gca,'FontSize',16)
