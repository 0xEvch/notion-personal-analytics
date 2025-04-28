from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from core.base.analyzer_core import AnalyzerCore

router = APIRouter()

@router.get("/summary")
async def get_summary(months_back: int = Query(..., description="Number of months to analyze")):
    try:
        analyzer = AnalyzerCore("autopilot")
        result = analyzer.run_analytics(months_back)
        
        response_data = {
            "status": "success",
            "data": {
                "statistics": result,
                # "chart": f"data:image/png;base64,{chart_base64}"
            }
        }
        return JSONResponse(content=jsonable_encoder(response_data))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing analytics: {str(e)}"
        )
    
# curl -X GET "http://localhost:8000/api/autopilot/summary?months_back=3" -H "accept: application/json"