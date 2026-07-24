# 易幺

> 小米手环 9 Pro（VelaOS）梅花易数时间起卦快应用

基于当前时间的年、月、日、时辰，以梅花易数法自动起卦，展示本卦、互卦、变卦及卦辞断语。另附阴历时间查询功能。

## 功能

- **一键起卦** — 根据当前时间自动计算上卦、下卦、动爻，生成本卦/互卦/变卦，可点击切换查看
  <img width="426" height="855" alt="Vela_Virtual_Device-2026-07-24-09-39-02" src="https://github.com/user-attachments/assets/c990922a-8411-4984-b092-02af58a0208e" />

- **卦辞展示** — 每卦显示卦辞、象曰、断语
  <img width="426" height="855" alt="Vela_Virtual_Device-2026-07-24-09-38-41" src="https://github.com/user-attachments/assets/e746c40c-a5d7-4b7e-8efc-8c347b2fa591" />

- **阴历时间** — 实时显示农历日期、干支（年/月/日分三行清晰展示）、时辰、公历日期
  <img width="426" height="855" alt="Vela_Virtual_Device-2026-07-24-09-38-51" src="https://github.com/user-attachments/assets/98ecf809-96d5-4043-a511-08fa7403b793" />

- **后天八卦** — 展示后天八卦方位图（离南坎北、震东兑西等）
  ![Uploading Vela_Virtual_Device-2026-07-24-09-38-56.png…]()


## 技术栈

- **平台**：VelaOS 快应用（`.ux` 单文件组件）
- **构建工具**：aiot-toolkit 2.0
- **目标设备**：小米手环 9 Pro（336×480）
- **无第三方依赖**：纯原生组件，农历转换与六十四卦数据库内嵌

## 构建

```bash
npm install
npm run build
```

生成的 RPK 包位于 `dist/` 目录，通过调试器安装到手环即可。

## 项目结构

```
src/
├── manifest.json          # 快应用配置（路由、设备、权限）
├── app.ux                 # 应用入口
├── i18n/
│   └── defaults.json      # 默认 i18n 资源
├── common/
│   ├── logo.png           # 应用图标
│   └── trigrams/          # 八卦符号 PNG（手表字体不支持 Unicode 卦符）
│       ├── qian.png
│       ├── dui.png
│       ├── li.png
│       ├── zhen.png
│       ├── xun.png
│       ├── kan.png
│       ├── gen.png
│       └── kun.png
└── pages/
    └── index/
        └── index.ux       # 主页面（四视图切换：主界面/阴历/后天八卦/结果）
```

## 起卦算法

采用梅花易数时间起卦法：

```
上卦 = (年数 + 月 + 日) % 8
下卦 = (年数 + 月 + 日 + 时) % 8
动爻 = (年数 + 月 + 日 + 时) % 6
```

- 互卦：取本卦第 2/3/4 爻为下卦，第 3/4/5 爻为上卦
- 变卦：将本卦动爻阴阳互换

## License

MIT
