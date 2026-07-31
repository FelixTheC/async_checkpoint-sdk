from .pydantic import BaseModel, Field


class VpnGlobalPropertiesReply(BaseModel):
    vpn_conf_method: str = Field(
        alias="vpn-conf-method",
        description="""Decide on Simplified or Traditional mode for all new security policies or decide which mode to use on a policy by policy basis.""",
    )
    domain_name_for_dns_resolving: str = Field(
        alias="domain-name-for-dns-resolving",
        description="""Enter the domain name that will be used for gateways DNS lookup. The DNS host name that is used is gateway_name.domain_name.""",
    )
    enable_backup_gw: bool = Field(
        alias="enable-backup-gw", description="""Enable Backup Gateway."""
    )
    enable_decrypt_on_accept_for_gw_to_gw_traffic: bool = Field(
        alias="enable-decrypt-on-accept-for-gw-to-gw-traffic",
        description="""Enable decrypt on accept for gateway to gateway traffic. This is only relevant for policies in traditional mode. In Traditional Mode, the 'Accept' action determines that a connection is allowed, while the 'Encrypt' action determines that a connection is allowed and encrypted. Select whether VPN accepts an encrypted packet that matches a rule with an 'Accept' action or drops it.""",
    )
    enable_load_distribution_for_mep_conf: bool = Field(
        alias="enable-load-distribution-for-mep-conf",
        description="""Enable load distribution for Multiple Entry Points configurations (Site To Site connections). The VPN Multiple Entry Point (MEP) feature supplies high availability and load distribution for Check Point Security Gateways. MEP works in four modes:<br>&nbsp;&nbsp;&nbsp;&nbsp; <ul><li> First to Respond, in which the first gateway to reply to the peer gateway is chosen. An organization would choose this option if, for example, the organization has two gateways in a MEPed configuration - one in London, the other in New York. It makes sense for Check Point Security Gateway peers located in England to try the London gateway first and the NY gateway second. Being geographically closer to Check Point Security Gateway peers in England, the London gateway will be the first to respond, and becomes the entry point to the internal network.</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li> VPN Domain, is when the destination IP belongs to a particular VPN domain, the gateway of that domain becomes the chosen entry point. This gateway becomes the primary gateway while other gateways in the MEP configuration become its backup gateways.</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li> Random Selection, in which the remote Check Point Security Gateway peer randomly selects a gateway with which to open a VPN connection. For each IP source/destination address pair, a new gateway is randomly selected. An organization might have a number of machines with equal performance abilities. In this case, it makes sense to enable load distribution. The machines are used in a random and equal way.</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li> Manually set priority list, gateway priorities can be set manually for the entire community or for individual satellite gateways.</li></ul>.""",
    )
    enable_vpn_directional_match_in_vpn_column: bool = Field(
        alias="enable-vpn-directional-match-in-vpn-column",
        description="""Enable VPN Directional Match in VPN Column.<br>Note: VPN Directional Match is supported only on Gaia, SecurePlatform, Linux and IPSO.""",
    )
    grace_period_after_the_crl_is_not_valid: int = Field(
        alias="grace-period-after-the-crl-is-not-valid",
        description="""When establishing VPN tunnels, the peer presents its certificate for authentication. The clock on the gateway machine must be synchronized with the clock on the Certificate Authority machine. Otherwise, the Certificate Revocation List (CRL) used for validating the peer's certificate may be considered invalid and thus the authentication fails. To resolve the issue of differing clock times, a Grace Period permits a wider window for CRL validity.""",
    )
    grace_period_before_the_crl_is_valid: int = Field(
        alias="grace-period-before-the-crl-is-valid",
        description="""When establishing VPN tunnels, the peer presents its certificate for authentication. The clock on the gateway machine must be synchronized with the clock on the Certificate Authority machine. Otherwise, the Certificate Revocation List (CRL) used for validating the peer's certificate may be considered invalid and thus the authentication fails. To resolve the issue of differing clock times, a Grace Period permits a wider window for CRL validity.""",
    )
    grace_period_extension_for_secure_remote_secure_client: int = Field(
        alias="grace-period-extension-for-secure-remote-secure-client",
        description="""When dealing with remote clients the Grace Period needs to be extended. The remote client sometimes relies on the peer gateway to supply the CRL. If the client's clock is not synchronized with the gateway's clock, a CRL that is considered valid by the gateway may be considered invalid by the client.""",
    )
    support_ike_dos_protection_from_identified_src: str = Field(
        alias="support-ike-dos-protection-from-identified-src",
        description="""When the number of IKE negotiations handled simultaneously exceeds a threshold above VPN's capacity, a gateway concludes that it is either under a high load or experiencing a Denial of Service attack. VPN can filter out peers that are the probable source of the potential Denial of Service attack. There are two kinds of protection:<br>&nbsp;&nbsp;&nbsp;&nbsp; <ul><li> Stateless - the peer has to respond to an IKE notification in a way that proves the peer's IP address is not spoofed. If the peer cannot prove this, VPN does not allocate resources for the IKE negotiation</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li> Puzzles - this is the same as Stateless, but in addition, the peer has to solve a mathematical puzzle. Solving this puzzle consumes peer CPU resources in a way that makes it difficult to initiate multiple IKE negotiations simultaneously.</li></ul>Puzzles is more secure then Stateless, but affects performance.<br>Since these kinds of attacks involve a new proprietary addition to the IKE protocol, enabling these protection mechanisms may cause difficulties with non Check Point VPN products or older versions of VPN.""",
    )
    support_ike_dos_protection_from_unidentified_src: str = Field(
        alias="support-ike-dos-protection-from-unidentified-src",
        description="""When the number of IKE negotiations handled simultaneously exceeds a threshold above VPN's capacity, a gateway concludes that it is either under a high load or experiencing a Denial of Service attack. VPN can filter out peers that are the probable source of the potential Denial of Service attack. There are two kinds of protection:<br>&nbsp;&nbsp;&nbsp;&nbsp; <ul><li> Stateless - the peer has to respond to an IKE notification in a way that proves the peer's IP address is not spoofed. If the peer cannot prove this, VPN does not allocate resources for the IKE negotiation</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li> Puzzles - this is the same as Stateless, but in addition, the peer has to solve a mathematical puzzle. Solving this puzzle consumes peer CPU resources in a way that makes it difficult to initiate multiple IKE negotiations simultaneously.</li></ul>Puzzles is more secure then Stateless, but affects performance.<br>Since these kinds of attacks involve a new proprietary addition to the IKE protocol, enabling these protection mechanisms may cause difficulties with non Check Point VPN products or older versions of VPN.""",
    )
