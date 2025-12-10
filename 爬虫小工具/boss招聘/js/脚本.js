(function() {
    // 获取并显示当前的__zp_stoken__
    function getToken() {
        const match = document.cookie.match(/__zp_stoken__=([^;]+)/);
        return match ? match[1] : '未找到__zp_stoken__';
    }

    // 显示当前Token值
    console.log('当前__zp_stoken__:', getToken());

    // 生成5-10秒之间的随机时间（单位：毫秒）
    const randomTime = Math.floor(Math.random() * 5000) + 50000;

    // 显示倒计时
    console.log(`将在${randomTime/1000}秒后刷新页面...`);

    // 设置定时器刷新页面
    setTimeout(() => {
        console.log('刷新页面...');
        location.reload();
    }, randomTime);
})();