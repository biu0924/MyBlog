<mxfile host="app.diagrams.net">
  <diagram name="业务流程图">
    <mxGraphModel dx="1242" dy="755" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- 用户注册和登录流程 -->
        <mxCell id="2" value="用户访问注册/登录页面" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="60" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="3" value="填写信息并提交" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="240" y="60" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="4" value="系统验证信息有效性" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="400" y="60" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="5" value="存入MySQL数据库" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="560" y="60" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="6" value="生成并返回会话Token" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="720" y="60" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="7" value="用户访问个人资料页面" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="880" y="60" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="8" value="查看或编辑资料" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1040" y="60" width="140" height="60" as="geometry" />
        </mxCell>

        <!-- 用户注册和登录流程连线 -->
        <mxCell id="9" edge="1" source="2" target="3" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="10" edge="1" source="3" target="4" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="11" edge="1" source="4" target="5" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="12" edge="1" source="5" target="6" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="13" edge="1" source="6" target="7" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="14" edge="1" source="7" target="8" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 文章发布和管理流程 -->
        <mxCell id="15" value="用户登录并访问文章管理页面" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="180" width="180" height="60" as="geometry" />
        </mxCell>
        <mxCell id="16" value="选择新建文章" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="280" y="180" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="17" value="填写文章内容并提交" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="440" y="180" width="180" height="60" as="geometry" />
        </mxCell>
        <mxCell id="18" value="系统验证文章内容有效性" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="640" y="180" width="180" height="60" as="geometry" />
        </mxCell>
        <mxCell id="19" value="存入MySQL数据库" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="840" y="180" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="20" value="用户可以编辑或删除文章" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1000" y="180" width="180" height="60" as="geometry" />
        </mxCell>

        <!-- 文章发布和管理流程连线 -->
        <mxCell id="21" edge="1" source="15" target="16" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="22" edge="1" source="16" target="17" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="23" edge="1" source="17" target="18" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="24" edge="1" source="18" target="19" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="25" edge="1" source="19" target="20" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 文章浏览和评论流程 -->
        <mxCell id="26" value="用户访问文章列表页面" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="300" width="180" height="60" as="geometry" />
        </mxCell>
        <mxCell id="27" value="选择文章阅读" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="280" y="300" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="28" value="系统从Redis获取文章详情" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="440" y="300" width="200" height="60" as="geometry" />
        </mxCell>
        <mxCell id="29" value="若无缓存则从MySQL获取并缓存" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="660" y="300" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="30" value="用户阅读文章" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="920" y="300" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="31" value="用户发表评论" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="1080" y="300" width="140" height="60" as="geometry" />
        </mxCell>
        <mxCell id="32" value="存入MySQL数据库并更新Redis" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
            <!-- 文章浏览和评论流程连线 -->
    <mxCell id="34" edge="1" source="26" target="27" parent="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    <mxCell id="35" edge="1" source="27" target="28" parent="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    <mxCell id="36" edge="1" source="28" target="29" parent="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    <mxCell id="37" edge="1" source="29" target="30" parent="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    <mxCell id="38" edge="1" source="30" target="31" parent="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    <mxCell id="39" edge="1" source="31" target="32" parent="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    <mxCell id="40" edge="1" source="32" target="33" parent="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
  </root>
    </mxGraphModel>
  </diagram>
</mxfile>