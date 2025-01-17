# Model for Silicon MEAM with original parameters for Si (Z=14)

from quippy import Potential

# A module defining a module needs to define only one variable,
# named `calculator`, which should be an instance of the ase.calculator.Calculator,
# a subclass of this, or a compatible class implementing the calculator interface.

calculator = Potential('IP Si_MEAM', param_str="""
<Si_MEAM_params n_types="1" label="">
<!-- Thomas J Lenosky, Babak Sadigh, Eduardo Alonso, Vasily V Bulatov, Tomas Diaz de la Rubia -->
<!-- Jeongnim Kim, Arthur F Voter and Joel D Kress -->
<!-- Highly optimized empirical potential model of silicon -->
<!-- Modelling Simul. Mater. Sci. Eng. 8 (2000) 825-841 -->
  <per_type_data atomic_num="14" type="1">
    <spline spline_function="U" n_spline="8" yp1="0.73514" ypn="0.61652">
      <point x="-1.7709300000" y="-1.0749300000" />
      <point x="-0.3881514286" y="-0.2004500000" />
      <point x=" 0.9946271429" y=" 0.4142200000" />
      <point x=" 2.3774057143" y=" 0.8793900000" />
      <point x=" 3.7601842857" y=" 1.2668900000" />
      <point x=" 5.1429628571" y=" 1.6299800000" />
      <point x=" 6.5257414286" y=" 1.9773800000" />
      <point x=" 7.9085200000" y=" 2.3961800000" />
    </spline>
  </per_type_data>
  <per_pair_data atomic_num_i="14" atomic_num_j="14" r_cut_phi="4.5" r_cut_rho="3.5" r_cut_f="3.5">
    <spline spline_function="phi" n_spline="10" yp1="-42.66967" ypn="0.00000">
      <point x="1.5000000000" y=" 6.9299400000" />
      <point x="1.8333333333" y="-0.4399500000" />
      <point x="2.1666666667" y="-1.7012300000" />
      <point x="2.5000000000" y="-1.6247300000" />
      <point x="2.8333333333" y="-0.9969600000" />
      <point x="3.1666666667" y="-0.2739100000" />
      <point x="3.5000000000" y="-0.0249900000" />
      <point x="3.8333333333" y="-0.0178400000" />
      <point x="4.1666666667" y="-0.0096100000" />
      <point x="4.5000000000" y=" 0.0000000000" />
    </spline>
    <spline spline_function="rho" n_spline="11" yp1="-1.00000" ypn="0.00000">
      <point x="1.5000000000" y=" 0.1374700000" />
      <point x="1.7000000000" y="-0.1483100000" />
      <point x="1.9000000000" y="-0.5597200000" />
      <point x="2.1000000000" y="-0.7311000000" />
      <point x="2.3000000000" y="-0.7628300000" />
      <point x="2.5000000000" y="-0.7291800000" />
      <point x="2.7000000000" y="-0.6662000000" />
      <point x="2.9000000000" y="-0.5732800000" />
      <point x="3.1000000000" y="-0.4069000000" />
      <point x="3.3000000000" y="-0.1666200000" />
      <point x="3.5000000000" y=" 0.0000000000" />
    </spline>
    <spline spline_function="f" n_spline="10" yp1="-3.61894" ypn="0.00000">
      <point x="1.5000000000" y="1.2503100000" />
      <point x="1.7222222222" y="0.8682100000" />
      <point x="1.9444444444" y="0.6084600000" />
      <point x="2.1666666667" y="0.4875600000" />
      <point x="2.3888888889" y="0.4416300000" />
      <point x="2.6111111111" y="0.3761000000" />
      <point x="2.8333333333" y="0.2714500000" />
      <point x="3.0555555556" y="0.1481400000" />
      <point x="3.2777777778" y="0.0485500000" />
      <point x="3.5000000000" y="0.0000000000" />
    </spline>
  </per_pair_data>
  <per_triplet_data atomic_num_i="14" atomic_num_j="14" atomic_num_k="14">
    <spline spline_function="g" n_spline="8" yp1="-13.95042" ypn="1.13462">
      <point x="-1.0000000000" y="5.2541600000" />
      <point x="-0.7428371429" y="2.3591500000" />
      <point x="-0.4856742857" y="1.1959500000" />
      <point x="-0.2285114286" y="1.2299500000" />
      <point x=" 0.0286514286" y="2.0356500000" />
      <point x=" 0.2858142857" y="3.4247400000" />
      <point x=" 0.5429771429" y="4.9485900000" />
      <point x=" 0.8001400000" y="5.6179900000" />
    </spline>
  </per_triplet_data>
</Si_MEAM_params>
""")

no_checkpoint = True
name = 'MEAM'
