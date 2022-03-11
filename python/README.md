### scikit-surpise install error 해결 - Surprise는 추천 시스템을 위한 사용하기 쉬운 scikit 라이브러리
-- install VisualStudio first, https://visualstudio.microsoft.com/downloads/ -- <br>
-> 맨 아래 쪽에 "재배포 가능 패키지 및 빌드 도구"  영역 선택 <br>
-> Microsoft Build Tools 2015 업데이트 3 클릭 후 설치 <br>
-> VS community 최근본 설치 후 rebooting <br>

* pip install wheel
* pip install scikit-surprise <br>
--- error message like belows--- <br>
ERROR: Failed building wheel for scikit-surprise
note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure <br>
error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio": https://visualstudio.microsoft.com/downloads/
      [end of output]<br>
------------------------ <br>

### OrderedDict
-- 파이썬 3.6 부터는 기본 사전(dict)도 OrderedDict 클래스와 동일하게 동작
* [설명](https://www.daleseo.com/python-collections-ordered-dict/)
