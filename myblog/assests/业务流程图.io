<mxfile host="app.diagrams.net">
  <diagram name="业务流程图">
    <mxGraphModel dx="1316" dy="798" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- 用户模块 -->
        <mxCell id="2" value="用户模块" style="swimlane;childLayout=stackLayout;horizontal=1;startSize=20;fillColor=#ffffff;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeParentMin=0;collapsible=0;" vertex="1" parent="1">
          <mxGeometry x="20" y="20" width="280" height="240" as="geometry" />
        </mxCell>
        <mxCell id="3" value="用户注册" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="2">
          <mxGeometry x="90" y="40" width="100" height="40" as="geometry" />
        </mxCell>
        <mxCell id="4" value="用户登录" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="2">
          <mxGeometry x="90" y="100" width="100" height="40" as="geometry" />
        </mxCell>
        <mxCell id="5" value="用户信息管理" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="2">
          <mxGeometry x="90" y="160" width="100" height="40" as="geometry" />
        </mxCell>
        <!-- 文章模块 -->
        <mxCell id="6" value="文章模块" style="swimlane;childLayout=stackLayout;horizontal=1;startSize=20;fillColor=#ffffff;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeParentMin=0;collapsible=0;" vertex="1" parent="1">
          <mxGeometry x="320" y="20" width="280" height="320" as="geometry" />
        </mxCell>
        <mxCell id="7" value="发布文章" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="6">
          <mxGeometry x="90" y="40" width="100" height="40" as="geometry" />
        </mxCell>
        <mxCell id="8" value="编辑文章" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="6">
          <mxGeometry x="90" y="100" width="100" height="40" as="geometry" />
        </mxCell>
        <mxCell id="9" value="删除文章" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="6">
          <mxGeometry x="90" y="160" width="100" height="40" as="geometry" />
        </mxCell>
        <mxCell id="10" value="文章展示" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="6">
          <mxGeometry x="90" y="220" width="100" height="40" as="geometry" />
        </mxCell>
        <!-- 评论模块 -->
        <mxCell id="11" value="评论模块" style="swimlane;childLayout=stackLayout;horizontal=1;startSize=20;fillColor=#ffffff;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeParentMin=0;collapsible=0;" vertex="1" parent="1">
          <mxGeometry x="620" y="20" width="280" height="160" as="geometry" />
        </mxCell>
        <mxCell id="12" value="发布评论" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="11">
          <mxGeometry x="90" y="40" width="100" height="40" as="geometry" />
        </mxCell>
        <mxCell id="13" value="评论展示" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="11">
          <mxGeometry x="90" y="100" width="100" height="40" as="geometry" />
        </mxCell>
        <!-- 流程连接 -->
        <mxCell id="14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="3" target="4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="4" target="5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="5" target="7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="17" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="7" target="8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="18" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="8" target="9">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="19" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="9" target="10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="20" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="10" target="12">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="21" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="12" target="13">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
