// 环境检测与适配
const isBrowser = typeof window !== 'undefined';
const root = isBrowser ? window : global;

// 可选：在 Node.js 中模拟浏览器环境（需要安装 jsdom）
if (!isBrowser) {
  try {
    const { JSDOM } = require('jsdom');
    const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>');

    // 模拟浏览器全局对象
    global.window = dom.window;
    global.document = dom.window.document;
    global.navigator = dom.window.navigator;
    global.location = dom.window.location;
    global.history = dom.window.history;
    global.screen = dom.window.screen;

    // 模拟存储对象
    class Storage {
      constructor() {
        this.store = {};
      }
      getItem(key) {
        return this.store[key] || null;
      }
      setItem(key, value) {
        this.store[key] = String(value);
      }
      removeItem(key) {
        delete this.store[key];
      }
      clear() {
        this.store = {};
      }
    }

    global.localStorage = new Storage();
    global.sessionStorage = new Storage();

    console.log('已在 Node.js 中模拟浏览器环境');
  } catch (error) {
    console.log('未安装 jsdom，跳过环境模拟');
    console.log('如需模拟浏览器环境，请运行: npm install jsdom');
  }
}

// 为指定对象数组里的对象创建 Proxy 代理
function setProxyArr(proxyObjArr) {
  for (let i = 0; i < proxyObjArr.length; i++) {
    const objName = proxyObjArr[i];

    // 检测对象是否存在
    if (typeof root[objName] === 'undefined') {
      console.log(`对象 ${objName} 不存在于当前环境，跳过创建 Proxy`);
      continue;
    }

    const handler = {
      get(target, property, receiver) {
        console.log(
          "方法:", "get",
          "对象:", objName,
          "属性:", property,
          "属性类型:", typeof property
        );
        return target[property];
      },
      set(target, property, value, receiver) {
        console.log(
          "方法:", "set",
          "对象:", objName,
          "属性:", property,
          "新值:", value
        );
        target[property] = value;
        return true;
      }
    };

    // 为目标对象创建 Proxy 并挂载到全局
    root[objName] = new Proxy(root[objName], handler);
  }
}

// 要代理的全局对象名称数组
const targetObjNames = [
  "window", "document", "navigator",
  "location", "history", "screen",
  "localStorage", "sessionStorage"
];

// 检测环境中缺少的对象
const missingObjects = [];
targetObjNames.forEach(objName => {
  if (typeof root[objName] === 'undefined') {
    missingObjects.push(objName);
  }
});

console.log('环境中缺少的对象:', missingObjects);

// 执行代理函数
setProxyArr(targetObjNames);

// 封装与环境相关的功能
function getWindow() {
  if (!isBrowser) {
    throw new Error('window 对象仅在浏览器环境中可用');
  }
  return window;
}

function getDocument() {
  if (!isBrowser) {
    throw new Error('document 对象仅在浏览器环境中可用');
  }
  return document;
}

// 使用示例
try {
  const w = getWindow();
  console.log('当前环境支持 window 对象');
} catch (error) {
  console.log(error.message);
}

// 模拟浏览器环境中的操作
if (isBrowser) {
  // 浏览器环境特有的代码
  document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM 已加载');
  });
} else {
  // Node.js 环境特有的代码
  console.log('Node.js 环境中无法执行 DOM 操作');
}

// 示例：安全地使用 localStorage
function saveData(key, value) {
  try {
    if (typeof localStorage !== 'undefined') {
      localStorage.setItem(key, value);
      console.log(`数据已保存到 localStorage: ${key}`);
    } else {
      console.log('localStorage 不可用，数据未保存');
    }
  } catch (error) {
    console.error('保存数据时出错:', error.message);
  }
}

// 测试保存数据
saveData('testKey', 'testValue');

// 示例：安全地访问 window 对象
function logWindowLocation() {
  if (typeof window !== 'undefined') {
    console.log('当前 URL:', window.location.href);
  } else {
    console.log('window 对象不可用');
  }
}

logWindowLocation();