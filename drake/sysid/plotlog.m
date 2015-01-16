function plotlog(file_num)

data = load(strcat(num2str(file_num),'.mat'));

tpos = data.crazyflie_squ_ext(:,8);
pos = data.crazyflie_squ_ext(:,2:7);

tinput = data.crazyflie_input(:,6);
input = data.crazyflie_input(:,2:5);

subplot(2,1,1);
plot(tpos,pos);
title('Position over time');
ylim([-5 5]);

subplot(2,1,2);
plot(tinput,input);
title('Input over time');

end
