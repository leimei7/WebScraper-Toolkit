from bs4 import BeautifulSoup

def extract_content(html_content):
    """
    从 HTML 内容中提取政府采购中标公告的关键信息

    Args:
        html_content (str): HTML 内容字符串

    Returns:
        dict: 提取的结构化数据
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取页面标题
    title = soup.title.string.strip() if soup.title else ""

    # 提取公告发布时间
    pub_time_elem = soup.select_one('#pubTime')
    pub_time = pub_time_elem.text.strip() if pub_time_elem else ""

    # 提取核心内容区域（使用更通用的选择器）
    content_div = soup.select_one('div[class^="vF_detail_main"]')
    if not content_div:
        print("未找到内容区域")
        return None

    soup = BeautifulSoup(content_div.text, 'html.parser')
    pure_text = soup.get_text()

    # 清理多余空白（可选）
    pure_text = ' '.join(pure_text.split())

    return pure_text

def extract_content_test():
    html_content = """
       <!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="cache-control" content="no-cache">
<meta http-equiv="expires" content="0">
<meta name="SiteName" content="中国政府采购网" />
<meta name="SiteDomain" content="www.ccgp.gov.cn" />
<meta name="SiteIDCode" content="bm14000002" />
<meta name="ArticleTitle" content="济南大学中心校区学生公寓改造提升项目施工中标（成交）公告" /> 
<meta name="PubDate" content="2025-07-14 01:59" />
<meta name="ContentSource" content="中国政府采购网" />
<title>济南大学中心校区学生公寓改造提升项目施工中标（成交）公告</title>
<link href="/css/detail.css" rel="stylesheet" type="text/css" />
<script language="javascript" src="/js/jquery-3.2.1.min.js"></script>
<script language="javascript" src="//pub.ccgp.gov.cn/common/js/jquery.qrcode.min.js"></script>  
</head>
<body id="detail"><script id="keyparam" src="/_bot_sbu/sbu_fpcm.js">b220cb5b51b0940c0f343d37ebb48744</script><script id="keyt" src="/_bot_sbu/sbu_fpc.js">900</script><script>(function () { document.cookie = "HOY_TR=TLUCFENXQSYKGMRW,3784956CABDEF012,kqvfxsglwjmyzhub; max-age=31536000; path=/";document.cookie = "HBB_HC=3c1820f1643537e8be1dea54de8d8c793809485a57a3b836dc75cd1740f7a1f958ff1c0ed85a5c35c7a3830da131eb60c1; max-age=600; path=/"; })()</script><script src="/_ws_sbu/sbu_hc.js"></script>
<link href="//www.ccgp.gov.cn/css/inc.css" rel="stylesheet" type="text/css" />
<div class="v4incheadertop">
    <div class="v4incheadertop_tel_block">
        <div class="v4incheadertop_tel">
            <p class="cl">财政部唯一指定政府采购信息网络发布媒体 国家级政府采购专业网站</p><p class="cr">服务热线：400-810-1996  &nbsp; | &nbsp; 服务投诉：010-63819289</p>
        </div>
    </div>
    <div class="v4incheadertop_logosearch_block2">
        <div class="v4incheadertop_logosearch">
        <div class="searcharea1">
            <div class="logo_gh" style="margin-top:20px">
            <a href="#" class="ccgp"></a>
            <a href="#" class="ccgp2"></a>
            <a href="#" class="gmfw"></a>
            <a href="#" class="ccgp3"></a>
            </div>
        </div>

        <div class="searcharea2">
            <div class="sangong_bl"></div>

        </div></div>
    </div>
    <div class="v4incheadertop_nav_block">
        <div class="v4incheadertop_nav">
            <ul class="v4incheadertop_nav_ls">
                <li  id="ch_index" style="width:140px"><a href="//www.ccgp.gov.cn/">首页</a></li>
                <li id="ch_zcfg" style="width: 172px"><a href="//www.ccgp.gov.cn/zcfg/">政采法规</a></li>
                <li id="ch_gmfw" style="width:172px"><a href="//www.ccgp.gov.cn/gpsr/">购买服务</a></li>
                <li id="ch_jdjc" style="width:172px"><a href="//www.ccgp.gov.cn/jdjc/">监督检查</a></li>
                <li id="ch_xxgg" style="width:172px"><a href="//www.ccgp.gov.cn/xxgg/">信息公告</a></li>
                <li id="ch_gpa" style="width:172px"><a href="//www.ccgp.gov.cn/wtogpa/">国际专栏</a></li>
            </ul>
        </div>
    </div>
    <div class="clb"></div>
</div>

<div class="main">
<div class="main_container">




    <div class="vF_deail_currentloc mt10">
        <p>当前位置：<a href="../../../../" title="首页" class="CurrChnlCls">首页</a>&nbsp;&raquo;&nbsp;
                <a href="../../../" title="政采公告" class="CurrChnlCls">政采公告</a>&nbsp;&raquo;&nbsp;<a href="../../" title="地方公告" class="CurrChnlCls">地方公告</a>&nbsp;&raquo;&nbsp;<a href="../" title="中标公告" class="CurrChnlCls">中标公告</a></p>
    </div>
    <div class="vF_deail_maincontent">

<div class="vF_detail_main  pzln75">
            <div class="vF_detail_header"><h2 class="tc">济南大学中心校区学生公寓改造提升项目施 工中标（成交）公告</h2>
            <p class="tc"><span id="pubTime">2025年07月14日 01:59</span> 来源：<span id="sourceName"></span> 【<span id="printBtn">打印</span>】 <span id="shareTo"></span></p></div>
<!--contentTable-->
<div class='table'><h5>公告概要：</h5><table width='600' border='0' cellspacing='1' bgcolor='#bfbfbf' style='text-align:left;'><tr><td colspan='4'><b>公告信息：</b></td></tr><tr><td class='title' width='128'>采购项目名称</td><td colspan='3' width='430'>济南大学中心校区学生公寓改造提升项 目施工</td></tr><tr><td class='title'>品目</td><td colspan='3'><p></p></td></tr><tr><td class='title'>采购单位</td><td colspan='3'>济南大学,济南大学,济南大学,济南大学</td></tr><tr><td class='title'>行政区域</td><td width='168'>山东省</td><td class='title' width='128'>公告时间</td><td width='168'>2025年07月14日  01:59</td></tr><tr><td class='title'>评审专家名单</td><td colspan='3'> 标包A：刘守强、陆阳、曹建伟、高维清、刘飞、张真、刘晓丽,张真、标包B：刘守强、陆阳、曹建伟、高维 清、刘飞、张真、刘晓丽,张真、标包C：刘守强、陆阳、曹建伟、高维清、刘飞、张真、刘晓丽,张真、标包D：刘守强、陆阳、曹建伟、高维清、刘飞、张真、刘晓丽,张真</td></tr><tr><td class='title'>总中标金 额</td><td colspan='3'>￥10618.520389 万元（人民币）</td></tr><tr><td colspan="4"><b>联系人及联 系方式：</b></td></tr><tr><td class='title'>项目联系人</td><td colspan='3'>吕宁、陈晓楠</td></tr><tr><td class='title'>项目联系电话</td><td colspan='3'>13589097223、0531-82665067</td></tr><tr><td class='title' width='128'>采购单位</td><td width='430' colspan='3'>济南大学,济南大学,济南大 学,济南大学</td></tr><tr><td class='title'>采购单位地址</td><td colspan='3'>济南市南辛庄西路336 号(济南大学)</td></tr><tr><td class='title'>采购单位联系方式</td><td colspan='3'>0531-82765758( 济南大学)</td></tr><tr><td class='title'>代理机构名称</td><td colspan='3'>海逸恒安项目管理有限公司</td></tr><tr><td class='title'>代理机构地址</td><td colspan='3'>山东省济南市历下县（区）工业 南路68号号华润置地广场A5-6号楼26层、27层</td></tr><tr><td class='title'>代理机构联系方式</td><td colspan='3'>13589097223、0531-82665067</td></tr></table></div>
<!--contentTable-->
<div class="vF_detail_content_container">
            <div class="vF_detail_content">
                <table><tr style='height:40px'><td align=center><div align=center><input type='hidden' name='UnitId' size='30' maxsize='50' value='-1' class=textbox />济南大学中心校区学生公寓 改造提升项目施工中标（成交）结果公告</div><div align=center><input type='hidden' name='BuyKind' size='30' maxsize='50' value='11' class=textbox /><input type='hidden' name='NoticeType' size='30' value='5' class=textbox /></div></td></tr><tr style='height:40px'><td><b>一、项目编号：</b>SDGP370000000202502005150</td></tr><tr style='height:40px'><td><b>二、项目名称：</b>济南大学中心校区学生公寓改造提升项目施工</td></tr><tr style='height:40px'><td><b>三、中标（成交）信息：</b></td></tr><tr style='height:40px'><td valign=top><table id='NoticeDetail' cellspacing='0'cellpadding='1' width='100%' style='border-collapse: collapse' border='1'><tr style='height:40px'><td>标包：<u>A</u></td></tr><tr style='height:40px'><td>供应商名称：<u>中建八局第二建设有限公司</u></td></tr><tr style='height:40px'><td>供应商地址：<u>山东省济南市历下区文化东路16号中建文化城二期办公楼1单元17层</u></td></tr><tr style='height:40px'><td>中标（成交）金额：（可填写下浮率、折扣率或 费率）：<u>2837.861389万元</u></td></tr><tr style='height:40px'><td>标包：<u>B</u></td></tr><tr style='height:40px'><td>供应商名称：<u>中建八局东南建设有限公司</u></td></tr><tr style='height:40px'><td>供应商地址：<u>厦门市思明区观音山国际商务营运中心2号11楼01和04单元部分</u></td></tr><tr style='height:40px'><td>中标（成交）金额：（可填写下浮率、折扣率或费率）：<u>2767万元</u></td></tr><tr style='height:40px'><td>标包：<u>C</u></td></tr><tr style='height:40px'><td>供应商名称：<u>济南一建集团有限公司</u></td></tr><tr style='height:40px'><td>供应商地址：<u>济南市历城区工业北路295号</u></td></tr><tr style='height:40px'><td>中标（成交）金额：（可填写下浮率、折扣率或费 率）：<u>2578.659万元</u></td></tr><tr style='height:40px'><td>标包：<u>D</u></td></tr><tr style='height:40px'><td>供应商名称：<u>中铁十局集团有限公司</u></td></tr><tr style='height:40px'><td>供应商地址：<u>山东省济南市高新技术产业开发区舜泰广场7号楼</u></td></tr><tr style='height:40px'><td>中标（成交）金额：（可填写下浮率、折扣率或费率）：<u>2435万元</u></td></tr></table></td></tr><tr style='height:40px'><td><b>四、主要标的信息：</b></td></tr><tr style='height:40px'><td valign=top><table id='NoticeDetail' cellspacing='0'cellpadding='1' width='100%' style='border-collapse: collapse' border='1'><tr style='height:40px'><td>标包：<u>A</u></td></tr><tr style='height:40px'><td>名称：<u>6#7#9#23#27#学生公寓改造</u></td></tr><tr style='height:40px'><td>施工范围：<u>详见附件</u></td></tr><tr style='height:40px'><td>施工工期：<u>接采购人通知之日起35天内全部施工完毕并通过竣工验收</u></td></tr><tr style='height:40px'><td>项目经理：<u>李丽</u></td></tr><tr style='height:40px'><td>执业证书信息：<u>一级建造师鲁1372014201608704</u></td></tr><tr style='height:40px'><td>标包：<u>B</u></td></tr><tr style='height:40px'><td>名称：<u>3#5#24#25#28#学生公寓改造</u></td></tr><tr style='height:40px'><td>施工范围：<u>详见附件</u></td></tr><tr style='height:40px'><td>施工工期：<u>接采购人通知之日起35天内全部施工完毕并通过竣工验收</u></td></tr><tr style='height:40px'><td>项目经理：<u>林伟</u></td></tr><tr style='height:40px'><td>执业证书信息：<u>一级建造师 闽1352022202403274</u></td></tr><tr style='height:40px'><td>标包：<u>C</u></td></tr><tr style='height:40px'><td>名称：<u>4#8#22#30#学生公寓改造</u></td></tr><tr style='height:40px'><td>施工范围：<u>详见附件</u></td></tr><tr style='height:40px'><td>施工工期：<u>接采购人通知之日起35天内全部施工完毕并通过竣工验收</u></td></tr><tr style='height:40px'><td>项目经理：<u>李福 山</u></td></tr><tr style='height:40px'><td>执业证书信息：<u>一级建造师 鲁1372011201201148</u></td></tr><tr style='height:40px'><td>标包：<u>D</u></td></tr><tr style='height:40px'><td>名称：<u>1#2#21#学生公寓改造</u></td></tr><tr style='height:40px'><td>施工范围：<u>详见附件</u></td></tr><tr style='height:40px'><td>施工工期：<u>接采购人通知之日起35天内全部施工完毕并通过竣工验收</u></td></tr><tr style='height:40px'><td>项目经理：<u>祝桂真</u></td></tr><tr style='height:40px'><td>执业证书信息：<u>一级建造师 鲁1372019202000976</u></td></tr></table></td></tr><tr style='height:40px'><td><b>五、评审专家（单一来源采购人员）名单：</b>标包A：刘守强、陆阳、曹建伟、高维清、 刘飞、张真、刘晓丽,张真、标包B：刘守强、陆阳、曹建伟、高维清、刘飞、张真、刘晓丽,张真、标包C：刘守强、陆阳、曹建伟、高维清、刘飞、张真、刘晓丽,张真、标包D：刘守强、陆阳、曹建伟、高维清、刘飞、张真、刘晓丽,张真</td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;<u>标包A：中建八 局第二建设有限公司（85.39、88.89、88.89、89.39、89.39、90.89、91.39）、山东省装饰集团有限公司（76.81、83.31、83.81、84.31、84.31、85.81、89.31）、济南四建（集团）有限责任公司（78.84、82.84、84.34、85.34、85.84、85.84、88.84）、深圳市科源建设集团股份有限公司（77.77、81.77、84.27、84.27、85.27、87.27、88.77）、深圳市博大建设集团有限公司（75.5、78.5、82.5、83.0、84.0、85.0、87.0）、中国电建市政建设集团有限公司（72.91、72.91、75.91、79.41、80.91、81.41、83.41）、山东省建设建工（ 集团）有限责任公司（79.57、82.57、84.07、84.57、85.57、87.57、88.57）、山西恒业建设集团有限公司 （67.72、70.22、73.22、75.22、77.72、78.22、80.22）、中铁十局集团有限公司（82.01、85.51、85.51、86.51、87.01、90.01、90.51）、山东永厦建设有限公司（80.06、82.56、84.06、84.56、85.06、85.06、90.06）、济南能源工程集团有限公司（73.13、78.63、80.63、80.63、83.63、85.13、86.13）、山东一滕建设集团有限公司（76.63、81.63、83.13、83.63、84.63、86.13、87.13）、山东富泰建设工程有限公司（73.63、75.13、76.63、80.63、82.13、82.63、83.63）、山东民生建工集团有限公司（77.69、81.69、83.19、84.19、86.19、86.19、87.69）、山东凯鑫建设工程有限公司（77.32、77.82、80.82、81.32、84.32、85.82、87.32）、山东滨中建筑装饰集团有限公司（81.18、83.18、86.68、87.68、89.18、89.68、89.68）、山东高 速齐鲁建设集团有限公司（77.24、79.74、83.74、84.24、84.24、84.74、86.24）、中明建投建设集团有限 责任公司（73.22、75.72、77.72、78.22、78.22、80.22、80.72）、中化学交通建设集团建筑工程有限公司 （74.71、78.71、79.21、81.21、83.71、84.21、85.21）、济南市中城发建设管理集团有限公司（77.21、78.71、81.71、83.21、83.71、84.71、85.71）、山东恒沣建筑工程有限公司（70.08、78.08、79.08、82.08、82.58、83.08、84.08）、济南恒远建设工程有限公司（70.18、72.18、74.18、77.68、79.68、81.68、84.18）、中晋华泰建设有限公司（69.72、70.22、73.72、75.22、75.22、77.22、78.22）标包B：中建八局东南建设有限公司（83.13、85.13、86.13、86.13、87.63、87.63、91.13）、山东省装饰集团有限公司（76.18、82.68、83.18、83.68、83.68、85.18、88.68）、中建八局第二建设有限公司（84.79、88.29、88.29、88.79、88.79、90.29、90.79）、嘉林建设集团有限公司（78.5、79.0、82.5、85.0、85.5、85.5、89.0）、济南四 建（集团）有限责任公司（77.96、81.96、83.46、84.46、84.96、84.96、87.96）、深圳市博大建设集团有 限公司（75.27、78.27、82.27、82.77、83.77、84.77、86.77）、中国电建市政建设集团有限公司（72.08、72.08、75.08、78.58、80.08、80.58、82.58）、济南黄河路桥建设集团有限公司（68.14、71.14、72.14、73.64、73.64、77.64、78.14）、山东省建设建工（集团）有限责任公司（79.55、82.55、84.05、84.55、85.55、87.55、88.55）、山西恒业建设集团有限公司（67.12、69.62、72.62、74.62、77.12、77.62、79.62） 、中铁十局集团有限公司（81.37、84.87、84.87、85.87、86.37、89.37、89.87）、山东永厦建设有限公司 （80.04、82.54、84.04、84.54、85.04、85.04、90.04）、济南能源工程集团有限公司（72.5、78.0、80.0 、80.0、83.0、84.5、85.5）、山东一滕建设集团有限公司（76.18、81.18、82.68、83.18、84.18、85.68、86.68）、飞凡建设集团有限公司（75.33、76.33、80.33、82.33、82.83、84.33、86.33）、山东富泰建设工程有限公司（73.03、74.53、76.03、80.03、81.53、82.03、83.03）、山东民生建工集团有限公司（77.17、81.17、82.67、83.67、85.67、85.67、87.17）、山东凯鑫建设工程有限公司（76.67、77.17、80.17、80.67、83.67、85.17、86.67）、山东高速齐鲁建设集团有限公司（76.8、79.3、83.3、83.8、83.8、84.3、85.8 ）、中明建投建设集团有限责任公司（72.61、75.11、77.11、77.61、77.61、79.61、80.11）、中化学交通 建设集团建筑工程有限公司（73.9、77.9、78.4、80.4、82.9、83.4、84.4）、济南市中城发建设管理集团有限公司（77.26、78.76、81.76、83.26、83.76、84.76、85.76）、山东恒沣建筑工程有限公司（70.02、78.02、79.02、82.02、82.52、83.02、84.02）、中晋华泰建设有限公司（69.12、69.62、73.12、74.62、76.12 、76.62、77.62）、中建七局安装工程有限公司（71.99、73.99、77.49、78.49、79.99、82.99、83.49）标 包C：济南一建集团有限公司（83.14、84.64、86.14、87.64、88.14、89.64、93.14）、山东省装饰集团有限公司（75.79、82.29、82.79、83.29、83.29、84.79、88.29）、嘉林建设集团有限公司（78.03、78.53、84.53、85.03、85.03、85.53、88.53）、济南四建（集团）有限责任公司（77.95、81.95、83.45、84.45、84.95、84.95、87.95）、山东万林建设工程有限公司（78.5、80.0、83.5、84.5、85.0、87.5、89.0）、中国电 建市政建设集团有限公司（71.68、74.68、78.18、79.14、79.68、80.18、82.18）、山东三箭建设工程管理 有限公司（73.62、76.12、80.62、82.12、82.62、84.62、85.12）、山东省建设建工（集团）有限责任公司 （77.85、80.85、82.35、82.85、83.85、85.85、86.85）、中铁十局集团有限公司（80.97、84.47、84.47、85.47、85.97、88.97、89.47）、山东永厦建设有限公司（79.82、82.32、83.82、84.32、84.82、84.82、89.82）、济南能源工程集团有限公司（72.1、77.6、79.6、79.6、82.6、84.1、85.1）、中建三局集团有限公 司（74.46、78.96、81.46、81.46、82.46、85.46、85.96）、山东申岳建设有限公司（75.95、79.95、83.45、83.45、84.95、86.95、87.95）、山东凯鑫建设工程有限公司（76.17、76.67、79.67、80.17、83.17、84.67、86.17）、山东鲁控建工集团有限公司（72.33、73.83、78.83、79.83、79.83、82.33、82.83）、山东高速齐鲁建设集团有限公司（76.5、79.0、83.0、83.5、83.5、84.0、85.5）、中化学交通建设集团建筑工程有限公司（73.57、77.57、78.07、80.07、82.57、83.07、84.07）、山东晟远建工集团有限公司（73.09、75.59、81.59、82.09、82.59、83.09、85.59）、济南市中城发建设管理集团有限公司（76.8、78.3、81.3、82.8、83.3、84.3、85.3）、山东恒沣建筑工程有限公司（69.58、77.58、78.58、81.58、82.08、82.58、83.58 ）、中建四局第六建设有限公司（73.73、76.23、81.73、81.73、82.23、84.23、85.73）标包D：中铁十局集团有限公司（81.35、85.85、86.85、87.85、89.35、89.35、89.85）、山东省装饰集团有限公司（76.17、82.67、83.17、83.67、83.67、85.17、88.67）、山东省建设建工集团装饰装璜有限公司（74.77、78.27、82.27、82.77、83.27、84.27、86.27）、山东省林海装饰工程有限公司（73.92、77.42、81.42、81.92、81.92、82.92、85.42）、济南四建（集团）有限责任公司（78.36、82.36、83.86、84.86、85.36、85.36、88.36） 、北京市市政四建设工程有限责任公司（73.47、77.47、77.97、79.97、81.97、81.97、83.47）、济南一建 集团有限公司（83.45、84.95、85.95、86.45、87.95、89.95、90.45）、山东长箭建设集团有限公司（75.36、75.86、80.86、81.36、82.36、83.36、85.36）、深圳市科源建设集团股份有限公司（77.08、81.08、83.58、83.58、84.58、86.58、88.08）、山东万林建设工程有限公司（78.24、79.74、83.24、84.24、84.74、86.74、88.74）、中国电建市政建设集团有限公司（72.07、72.07、75.07、78.57、80.07、80.57、82.57）、 山东三箭建设工程管理有限公司（74.0、80.5、81.0、82.5、83.0、85.0、85.5）、深圳市建侨建工集团有限公司（75.48、78.98、81.48、81.98、83.48、85.48、85.98）、济南黄河路桥建设集团有限公司（67.11、71.11、73.61、73.61、74.11、77.61、78.11）、山东省建设建工（集团）有限责任公司（79.1、82.1、83.6、84.1、85.1、87.1、88.1）、中铁十四局集团有限公司（74.85、74.85、79.85、81.85、82.35、82.35、84.35）、山东永厦建设有限公司（80.5、83.0、84.5、85.0、85.5、85.5、90.5）、济南能源工程集团有限公司 （72.13、77.63、79.63、79.63、82.63、84.13、85.13）、山东福思特建筑装饰有限公司（70.44、73.94、78.44、78.94、79.44、80.94、82.94）、山东泉城建设集团有限公司（78.42、79.92、82.92、82.92、83.92 、84.92、87.42）、中国建筑第六工程局有限公司（73.96、77.96、81.46、82.46、82.46、83.96、85.46） 、山东凯鑫建设工程有限公司（76.64、77.14、80.14、80.64、83.64、85.14、86.64）、上海二十冶建设有 限公司（67.36、70.86、73.36、75.36、75.86、78.36、78.86）、鸿川建筑产业集团有限公司（76.35、79.35、81.35、82.85、83.85、85.35、86.85）、深圳市建筑装饰（集团）有限公司（76.69、78.19、83.69、83.69、84.19、84.19、86.19）、中化学交通建设集团建筑工程有限公司（73.95、77.95、78.45、80.45、82.95、83.45、84.45）、山东晟远建工集团有限公司（73.51、76.01、81.51、82.01、82.01、83.51、86.01）、 济南市中城发建设管理集团有限公司（76.33、77.83、80.83、82.33、82.83、83.83、84.83）、山东舜联城 市建设发展有限公司（78.39、79.39、82.89、83.89、83.89、84.39、85.89）、中建八局发展建设有限公司 （73.79、78.29、82.79、82.79、82.79、83.29、86.29）、山东恒沣建筑工程有限公司（69.21、77.21、78.21、81.21、81.71、82.21、83.21）、济南恒远建设工程有限公司（69.38、70.88、72.88、76.38、76.38、80.38、82.88）、中建四局第六建设有限公司（74.29、76.79、82.29、82.79、83.29、84.79、86.29）</td></tr><tr style='height:40px'><td><b>六、代理服务收费标准及金额：</b></td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;<b>收费标准：</b>成交服务费按“采购代理服务费收费标准”以差额累进法计算后下浮30%计取，由成交供应商向代理机构交纳</td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;<b>收费金额（单位：元）：</b>345552.00</td></tr>  <tr style='height:40px'><td><b>七、公告期限</b></td></tr><tr><td>&nbsp;&nbsp;&nbsp;&nbsp;自本公告发布之日起1个工作日。</td></tr><tr style='height:40px'><td><b>八、其他补充事宜：</b></td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;其他补充事宜：<u>无</td></tr><tr style='height:40px'><td><b>九、未中标（成交）供应商的未中标（成交）原因：</b></td></tr><tr style='height:40px'><td>1、济南市中城发建设管理集 团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>2、中 国建筑第二工程局有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>3、深圳市博大建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>4、深圳市科源建设集团股份有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>5、山东一滕建设集团有限公司：评审得分较低（其他情形综合评 审得分较低）</td></tr><tr style='height:40px'><td>6、华鑫盛建设集团有限公司：评审得分较低（其他 情形符合性审查不通过）</td></tr><tr style='height:40px'><td>7、济南四建（集团）有限责任公司：评 审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>8、山东凯鑫建设工程 有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>9、中化 学交通建设集团建筑工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>10、山东恒沣建筑工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>11、中国电建集团山东电力建设第一工程有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>12、昊晟集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>13、山东高速工程建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>14、中铁十局集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>15、中儒科信达建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>16、山东省建设建工（集团）有限责任公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>17、中明建投建设集团有限责任公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>18、中建五局装饰幕墙有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>19、山东省装饰集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>20、中晋华泰建设有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>21、山东高速齐鲁建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>22、山东滨中建筑装饰集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>23、济南能源工程集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>24、山西恒业建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>25、济南恒远建设工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>26、威海建设集团股份有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>27、山东永厦建设有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>28、山东丽天建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>29、山东富泰建设工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>30、山东民生建工集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>31、中国电建市政建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>32、山东永厦建设有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>33、济南恒远建设工程有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>34、中铁建大湾区建设有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>35、山东丽天建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>36、山东民生建工集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>37、山西恒业建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>38、中国电建市政建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>39、山东富泰建设工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>40、济南市中城发建设管理集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>41、深圳市博大建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>42、中建八局第二建设有限公司：评审得分较低（其他情形兼投不兼中）</td></tr><tr style='height:40px'><td>43、山东一滕建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>44、中建七局安装工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>45、济南黄河路桥建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>46、华鑫盛建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>47、济南四建（集团）有限责任公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>48、中化学交通建设集团建筑工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>49、山东恒沣建筑工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>50、嘉林建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>51、中国电建集团山东电力建设第一工程有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>52、山东凯鑫建设工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>53、山东高速工程建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>54、中儒科信达建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>55、山东省建设建工（集团）有限责任公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>56、中明建投建设集团有限责任公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>57、中铁十局集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>58、山东省装饰集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>59、中晋华泰建设有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>60、山东黄金集团建设工程有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>61、飞凡建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>62、济南能源工程集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>63、山东高速齐鲁建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>64、威海建设集团股份有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>65、中建三局集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>66、中国电建市政建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>67、山东三箭建设工程管理有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>68、济南市中城发建设管理集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>69、山东万林建设工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>70、山东申岳建设有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>71、济南四建（集团）有限责任公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>72、中化学交通建设集团建筑工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>73、山东恒沣建筑工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>74、嘉林建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>75、山东鲁控建工集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>76、中国电建集团山东电力建设第一工程有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>77、山东凯鑫建设工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>78、山东高速工程建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>79、中儒科信达建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>80、山东晟远建工集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>81、山东省建设建工（集团）有限责任公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>82、中建五局装饰幕墙有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>83、中铁十局集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>84、山东省装饰集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>85、济南能源工程集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>86、山东高速齐鲁建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>87、山东福思特建筑装饰有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>88、威海建设集团股份有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>89、山东永厦建设有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>90、济南恒远建设工程有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>91、山东丽天建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>92、中铁建大湾区建设有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>93、中建四局第六建设有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>94、山东凯鑫建设工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>95、中铁十四局集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>96、山东高速工程建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>97、中儒科信达建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>98、山东晟远建工集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>99、中国建筑第六工程局有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>100、山东省建设建工（集团）有 限责任公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>101、 上海二十冶建设有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>102、山东省装饰集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>103、山东泉城建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>104、深圳市建侨建工集团有限公司：评审得分较低（其他情形综合评审得 分较低）</td></tr><tr style='height:40px'><td>105、山东福思特建筑装饰有限公司：评审得分较低（其 他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>106、威海建设集团股份有限公司：评 审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>107、山东永厦建设有 限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>108、森特 建设集团有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>109、济南能源工程集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>110、济南恒远建设工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>111、中铁建大湾区建设有限公司：评审得分较低（其他情形符合性审查不通过 ）</td></tr><tr style='height:40px'><td>112、中建四局第六建设有限公司：评审得分较低（其他情形综 合评审得分较低）</td></tr><tr style='height:40px'><td>113、山东丽天建设集团有限公司：评审得分较 低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>114、山东舜联城市建设发展有 限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>115、深圳 市建筑装饰（集团）有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>116、山东省林海装饰工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>117、鸿川建筑产业集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>118、中国电建市政建设集团有限公司：评审得分较低（其他情形 综合评审得分较低）</td></tr><tr style='height:40px'><td>119、中建八局发展建设有限公司：评审得分 较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>120、山东三箭建设工程管理 有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>121、济 南市中城发建设管理集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>122、北京市市政四建设工程有限责任公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>123、山东万林建设工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>124、山东建勘集团有限公司：评审得分较低（其他情 形符合性审查不通过）</td></tr><tr style='height:40px'><td>125、山东泉景建设有限公司：评审得分较 低（其他情形资格审查未通过）</td></tr><tr style='height:40px'><td>126、深圳市科源建设集团股份有 限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>127、中化 学交通建设集团建筑工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>128、山东恒沣建筑工程有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>129、中国电建集团山东电力建设第一工程有限公司：评审得分较低（其他情形符合性审查不通过）</td></tr><tr style='height:40px'><td>130、济南一建集团有限公司：评审得分较低 （其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>131、济南黄河路桥建设集团有限 公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>132、山东省 建设建工集团装饰装璜有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>133、山东长箭建设集团有限公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td>134、济南四建（集团）有限责任公司：评审得分较低（其他情形综合评审得分较低）</td></tr><tr style='height:40px'><td><b>十、凡对本次公告内容提出询问，请按以下方式联系：</b></td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1、采购人信息</td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;名&nbsp;&nbsp;&nbsp;&nbsp;称：<u><input type='hidden' name='UnitCode' size='30' maxsize='50' value='140012' class=textbox />济南大学,济南大学,济南大学,济南大学</td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;地&nbsp;&nbsp;&nbsp;&nbsp;址：<u>济南市南辛庄西路336号(济南大学)</td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系方式：<u>0531-82765758(济南大学)</td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2、采购代理机构信息（如有）</td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;名&nbsp;&nbsp;&nbsp;&nbsp;称:<u><input type='hidden' name='AgentCode' size='30' maxsize='50' value='188' class=textbox />海逸恒安项目管理有限公 司</u></td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;地&nbsp;&nbsp;&nbsp;&nbsp;址：<u>山东省济南市历下县（区）工业南路68号号华润置地广场A5-6号楼26层、27 层</u></td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系方式：<u>13589097223、0531-82665067</u></td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3、项目联系方式</td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;项目联系人：<u>吕宁、陈晓楠</u></td></tr><tr style='height:40px'><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系方式：<u>13589097223、0531-82665067<input type='hidden' name='LinkMan' size='10' readonly value='吕宁、陈晓楠' /><input type='hidden' name='LinkTel' size='10' readonly value='13589097223、0531-82665067' /></u></td></tr><tr style='height:40px'><td><b>十一、附件：</b></td></tr></table>
            </div>
        </div><!--vF_detail_content_container-->
        </div><!--vF_detail_main-->


    </div><!--vF_deail_maincontent-->
    <div class="vF_detail_relcontent mt13">
    <h2><p>相关公告</p></h2>
    <div class="vF_detail_relcontent_lst">
        <ul class="c_list_tat">

        </ul>
    </div>
</div><!--相关公告-->

    </div>
</div>
</div>
<div class="footer mt13">

    <div class="copyright_bl">
<style type="text/css">
    .copyright_bl{width:1000px;margin:0 auto}/*margin-top:20px;*/
    .vF_cp {width: 1000px;margin: 0 auto;text-align: left;float: left;background: #e9e9e9;color: #333;height: 120px;padding-top: 10px;}
    .vF_cp p {width: 600px;float: left;margin-top: 15px;font-size: 14px;line-height: 26px;}     
    .vF_cp span{font-family:Verdana, Geneva, sans-serif;font-size:12px}
    .vF_cp a,.vT_cp a{color:#333;text-decoration: none}
    .vF_cp a:hover,.vT_cp a:hover{text-decoration: underline;color:#ba2636}
    .dzjg {width: 205px;height: 80px;float: left;margin: 14px 10px 0 130px;border-right: 1px solid #c2c2c2;}
    .cpright {float: left;width: 570px;margin-left: 15px;}
    .ccgpjiucuo{width:110px;height:55px;float:left;margin-left:5px;margin-top:10px}
    @media print {.main_container{float:left}}
    </style>
     <div class="vF_cp">
        <div class="dzjg">
            <div class="ccgpjiucuo">
                <a href="https://zfwzgl.www.gov.cn/exposure/jiucuo.html?site_code=bm14000002&amp;url=http%3A%2F%2Fwww.ccgp.gov.cn%2F" target="_blank"><img src="//www.ccgp.gov.cn/img/jiucuo.png"></a>
                </div>
            <script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='https://dcs.conac.cn/js/33/000/0000/60425889/CA330000000604258890010.js' type='text/javascript'%3E%3C/script%3E"));</script></div>
    <div class="cpright">
        <p>
        主办单位：中华人民共和国财政部国库司  <br>网站标识码：<span>bm14000002</span> &nbsp;|&nbsp; <a href="https://beian.miit.gov.cn" target="_blank">京<span>ICP</span>备<span>19054529</span>号<span>-1</span></a> &nbsp;|&nbsp; 京公网安备<span>11010602060068</span>号 <br><span id="botm_cpy">&copy; 1999-</span> 中华人民共和国财政部 版权所有 &nbsp;|&nbsp; <a href="/contact.shtml" target="_blank">联系我们</a> &nbsp;|&nbsp; <a href="//www.ccgp.gov.cn/zxly/" target="_blank">意见 反馈</a> </p>
    </div>
    </div>
    </div>
    <script language="javascript">
        var myDate = new Date();
        var botmcpy='&copy; 1999-'+ myDate.getFullYear();
        $("#botm_cpy").html(botmcpy);
        //document.getElementById(botm_cpy).innerHTML(botmcpy);
    </script>
    <script language="javascript" src="//www.ccgp.gov.cn/images/vr.js"></script>
    </div>
</div>
</body>
<script language="javascript" src="/js/detailaddon.js"></script>
</html>
       """
    return extract_content(html_content)

if __name__ == '__main__':
   print(extract_content_test())


data = \
{
"项目编号": "",
"项目名称": "",
"采购单位": "",
"中标供应商": {
"名称": "",
"地址": "",
"中标金额": "",
"评审得分": ""
},
"公告时间": ""
}

